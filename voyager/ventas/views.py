from django.shortcuts import render
from reportes.models import Analisis, Cotizacion, AnalisisCotizacion
from cuentas.models import IFCUsuario
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from django.http import Http404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import Http404
import json

# Create your views here.

# CÁTALOGO DE ANÁLISIS
@login_required
def ver_catalogo(request):
    user_logged = IFCUsuario.objects.get(user = request.user) # Obtener el tipo de usuario logeado
    if user_logged.rol.nombre == "Ventas" or user_logged.rol.nombre == "SuperUser":
        analisis = Analisis.objects.all()
        context = {
            'analisis': analisis,
        }
        return render(request, 'ventas/catalogo.html', context)
    else: # Si el rol del usuario no es ventas no puede entrar a la página
        raise Http404

@login_required
def cargar_analisis(request, id):
    user_logged = IFCUsuario.objects.get(user = request.user) # Obtener el tipo de usuario logeado
    if user_logged.rol.nombre == "Ventas" or user_logged.rol.nombre == "SuperUser":
        if request.method == 'POST':
            analisis = Analisis.objects.get(id_analisis = id)
            if analisis:
                data = serializers.serialize("json", [analisis], ensure_ascii = False)
                data = data[1:-1]
                return JsonResponse({"data": data})
            else:
                response = JsonResponse({"error": "No existe ese análisis"})
                response.status_code = 500
                # Regresamos la respuesta de error interno del servidor
                return response
        else:
            response = JsonResponse({"error": "No se mandó por el método correcto"})
            response.status_code = 500
            # Regresamos la respuesta de error interno del servidor
            return response
    else: # Si el rol del usuario no es ventas no puede entrar a la página
        raise Http404
    
@login_required
def editar_analisis(request, id):
    user_logged = IFCUsuario.objects.get(user = request.user) # Obtener el tipo de usuario logeado
    if user_logged.rol.nombre == "Ventas" or user_logged.rol.nombre == "SuperUser":
        # Checamos que el método sea POST
        if request.method == 'POST':
            # Obtenemos el objeto de análisis
            analisis = Analisis.objects.get(id_analisis = id)
            if analisis:
                #Que ningún campo esté vacío
                if is_not_empty(request.POST['nombre']) and is_not_empty(request.POST['codigo']) and is_not_empty(request.POST['descripcion']) and is_not_empty(request.POST['precio']) and is_not_empty(request.POST['tiempo']):
                    # Actualizamos campos
                    analisis.nombre = request.POST['nombre']
                    analisis.codigo = request.POST['codigo']
                    analisis.descripcion = request.POST['descripcion']
                    analisis.precio = request.POST['precio']
                    analisis.tiempo = request.POST['tiempo']
                    # Guardamos cambios
                    analisis.save()
                    # Obtenemos los nuevos valores
                    analisis_actualizado = Analisis.objects.get(id_analisis = id)
                    data = serializers.serialize("json", [analisis_actualizado], ensure_ascii = False)
                    data = data[1:-1]
                    # Regresamos información actualizada
                    return JsonResponse({"data": data})
                else:
                    response = JsonResponse({"error": "Campos vacíos"})
                    response.status_code = 500
                    # Regresamos la respuesta de error interno del servidor
                    return response
            else:
                response = JsonResponse({"error": "No existe ese análisis"})
                response.status_code = 500
                # Regresamos la respuesta de error interno del servidor
                return response
        else:
            response = JsonResponse({"error": "No se mandó por el método correcto"})
            response.status_code = 500
            # Regresamos la respuesta de error interno del servidor
            return response
    else: # Si el rol del usuario no es ventas no puede entrar a la página
        raise Http404
        
@login_required
def borrar_analisis(request, id):
    user_logged = IFCUsuario.objects.get(user = request.user) # Obtener el tipo de usuario logeado
    if user_logged.rol.nombre == "Ventas" or user_logged.rol.nombre == "SuperUser":
        # Checamos que el método sea POST
        if request.method == 'POST':
            # Obtenemos el objeto de análisis
            analisis = Analisis.objects.get(id_analisis = id)
            if analisis:
                analisis.delete()
                return HttpResponse('OK')
            else:
                response = JsonResponse({"error": "No existe ese análisis"})
                response.status_code = 500
                # Regresamos la respuesta de error interno del servidor
                return response
        else:
            response = JsonResponse({"error": "No se mandó por el método correcto"})
            response.status_code = 500
            # Regresamos la respuesta de error interno del servidor
            return response
    else: # Si el rol del usuario no es ventas no puede entrar a la página
        raise Http404

# Funciones para validar campos

# COTIZACIONES

# COTIZACIONES




# Cotizaciones

@login_required
def ver_cotizaciones(request):
    #Vista de cotizaciones del cliente
    context = {}
    if request.session._session:
        usuario_log = IFCUsuario.objects.filter(user=request.user).first() #Obtener usuario que inició sesión
        if usuario_log.rol.nombre == "Cliente" or usuario_log.rol.nombre == "Ventas" or usuario_log.rol.nombre == "SuperUser":
            if usuario_log.rol.nombre == "Ventas":
                cotizaciones = Cotizacion.objects.filter(usuario_v=usuario_log) #Obtener cotizaciones de usuario ventas
                analisis = Analisis.objects.all()
                context = {
                    'analisis': analisis,
                    'cotizaciones': cotizaciones
                }
            elif usuario_log.rol.nombre == "Cliente":
                cotizaciones = Cotizacion.objects.filter(usuario_c=usuario_log) #Obtener cotizaciones de usuario cliente
                context = {
                    'cotizaciones': cotizaciones,
                }
            elif usuario_log.rol.nombre == "SuperUser":
                cotizaciones = Cotizacion.objects.all()
                analisis = Analisis.objects.all()
                context = {
                    'analisis': analisis,
                    'cotizaciones': cotizaciones
                }
            return render(request, 'ventas/cotizaciones.html', context)
        else:
            raise Http404

# FUNCIONES EXTRA



def cargar_cot(request):
    user_logged = IFCUsuario.objects.get(user = request.user) # Obtener el tipo de usuario logeado
    if user_logged.rol.nombre == "Ventas" or user_logged.rol.nombre == "SuperUser":
        if request.method == 'POST':
            # Obtenemos el arreglo de análisis seleccionados para crear cotización
            checked = request.POST.getlist('checked[]')
            if checked:
                data = []
                # Iteramos en los análisis seleccionados
                for id in checked: #Asignar codigo DHL
                    analisis = Analisis.objects.get(id_analisis = id)
                    if analisis: #Valida si existe y lo añade al array
                        print(analisis.nombre)
                        data.append(analisis)
                    else:
                        response = JsonResponse({"error": "No existe ese análisis"})
                        response.status_code = 500
                        # Regresamos la respuesta de error interno del servidor
                        return response
                #return HttpResponse(json.dumps(data), content_type='application/json')
                info = serializers.serialize("json", data, ensure_ascii = False)
                return JsonResponse({"info": info})
            else:
                response = JsonResponse({"error": "No llegaron análisis seleccionados"})
                response.status_code = 500
                # Regresamos la respuesta de error interno del servidor
                return response
        else:
            response = JsonResponse({"error": "No se mandó por el método correcto"})
            response.status_code = 500
            # Regresamos la respuesta de error interno del servidor
            return response
    else: # Si el rol del usuario no es ventas no puede entrar a la página
        raise Http404
    
def is_not_empty(data):
    if data != "":
        return True
    else:
        return False
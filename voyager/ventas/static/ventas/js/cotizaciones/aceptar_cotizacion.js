//######### USV16-50 ########

/* Funciones que se ejecutan al cargar la página */
$(document).ready(function() {
    // Cuando se cierra el modal para confirmar el borrado de la cotizacion, reajusta la variable global a 0
    $('#aceptar_cot').on('hidden.bs.modal', function () {
       id_aceptar = 0;
    });
});


function aceptar_cotizacion(id){
    if (id > 0){
        id_aceptar = id;     // Carga el id de la cotización que se quiere aceptar en la variable global
    }
}

function confirmar_aceptar_cotizacion(){
    if (id_aceptar > 0){
        // Guardar variables globales en locales
        var id =  id_aceptar;
        var token = csrftoken;
        $.ajax({
            url: "aceptar_cotizacion/"+id,
            // Seleccionar información que se mandara al controlador
            data: {
                id:id,
                'csrfmiddlewaretoken': token
            },
            type: "POST",
            success: function(){
                aceptar_cotizacion_tabla('.cot-row',id);
                id_aceptar = 0;
                $('#aceptar_cot').modal('toggle');                                        // Cerrar el modal de aceptar cotizacion
                showNotificationSuccess('top','right','Se ha validado la cotización exitosamente.');
            },
        });

    }
 // Mostrar alerta de cotizacion borrada
}

function aceptar_cotizacion_tabla(clase,id){
    $(clase).each(function(i,e){
       if( $(e).data('id') == id ){
         $(e).find('#cotizacion_child_estado').html('Aceptado');
         $(e).find('#cotizacion_child_aceptar').prop('hidden', true);
       }
    });
}

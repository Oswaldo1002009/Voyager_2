# Generated by Django 2.2.5 on 2019-10-17 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cuentas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analisis',
            fields=[
                ('id_analisis', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=30)),
                ('tiempo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Paquete',
            fields=[
                ('id_paquete', models.AutoField(primary_key=True, serialize=False)),
                ('codigo_dhl', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrdenInterna',
            fields=[
                ('idOI', models.AutoField(primary_key=True, serialize=False)),
                ('localidad', models.CharField(blank=True, max_length=50)),
                ('fecha_envio', models.DateField(blank=True, null=True)),
                ('link_resultados', models.CharField(blank=True, max_length=300)),
                ('guia_envio', models.CharField(blank=True, max_length=50)),
                ('formato_ingreso_muestra', models.CharField(blank=True, choices=[('Sí', 'Sí'), ('No', 'No')], max_length=2)),
                ('idioma_reporte', models.CharField(blank=True, choices=[('8809 ES', '8809 ES'), ('8992 EN', '8992 EN')], max_length=20)),
                ('mrl', models.CharField(blank=True, max_length=200)),
                ('estatus', models.CharField(blank=True, choices=[('invisible', 'invisible'), ('fantasma', 'fantasma'), ('activo', 'activo')], max_length=15)),
                ('fecha_eri', models.DateField(blank=True, null=True)),
                ('notif_e', models.CharField(blank=True, choices=[('Sí', 'Sí'), ('No', 'No')], max_length=2)),
                ('fecha_lab', models.DateField(blank=True, null=True)),
                ('fecha_ei', models.DateField(blank=True, null=True)),
                ('envio_ti', models.CharField(blank=True, choices=[('Sí', 'Sí'), ('No', 'No')], max_length=2)),
                ('cliente_cr', models.CharField(blank=True, choices=[('Sí', 'Sí'), ('No', 'No')], max_length=2)),
                ('resp_pago', models.CharField(blank=True, max_length=50)),
                ('correo', models.EmailField(blank=True, max_length=50)),
                ('telefono', models.CharField(blank=True, max_length=13)),
                ('paquete', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reportes.Paquete')),
                ('usuario', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cuentas.IFCUsuario')),
            ],
            options={
                'verbose_name': 'Orden Interna',
                'verbose_name_plural': 'Órdenes Internas',
            },
        ),
        migrations.CreateModel(
            name='Muestra',
            fields=[
                ('id_muestra', models.AutoField(primary_key=True, serialize=False)),
                ('producto', models.CharField(max_length=50)),
                ('variedad', models.CharField(max_length=50)),
                ('pais_origen', models.CharField(max_length=50)),
                ('codigo_muestra', models.CharField(max_length=50)),
                ('agricultor', models.CharField(max_length=50)),
                ('ubicacion', models.CharField(max_length=75)),
                ('estado', models.CharField(max_length=20)),
                ('parcela', models.CharField(max_length=50)),
                ('fecha_muestreo', models.DateField()),
                ('destino', models.CharField(max_length=50)),
                ('idioma', models.CharField(max_length=20)),
                ('estado_muestra', models.BooleanField()),
                ('fechah_recibo', models.DateTimeField(blank=True, null=True)),
                ('fecha_forma', models.DateField()),
                ('oi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.OrdenInterna')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuentas.IFCUsuario')),
            ],
        ),
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id_cotizacion', models.AutoField(primary_key=True, serialize=False)),
                ('descuento', models.DecimalField(decimal_places=4, max_digits=100)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=100)),
                ('iva', models.DecimalField(decimal_places=2, max_digits=100)),
                ('total', models.DecimalField(decimal_places=2, max_digits=100)),
                ('status', models.BooleanField()),
                ('usuario_c', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to='cuentas.IFCUsuario')),
                ('usuario_v', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ventas', to='cuentas.IFCUsuario')),
            ],
        ),
        migrations.CreateModel(
            name='AnalisisMuestra',
            fields=[
                ('id_analisis_muestra', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField()),
                ('fecha', models.DateField()),
                ('analisis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Analisis')),
                ('muestra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Muestra')),
            ],
        ),
        migrations.CreateModel(
            name='AnalisisCotizacion',
            fields=[
                ('id_analisis_cotizacion', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateField()),
                ('analisis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Analisis')),
                ('cotizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Cotizacion')),
            ],
        ),
    ]

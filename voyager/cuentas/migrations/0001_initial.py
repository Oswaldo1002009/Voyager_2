# Generated by Django 2.1.7 on 2019-10-22 19:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Rol',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='IFCUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido_paterno', models.CharField(max_length=30)),
                ('apellido_materno', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=15)),
                ('estado', models.BooleanField(default=True)),
                ('empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cuentas.Empresa')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuentas.Rol')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('estatus_pago', models.CharField(default='NA', max_length=10)),
            ],
            options={
                'verbose_name': 'Usuario IFC',
                'verbose_name_plural': 'Usuarios IFC',
            },
        ),
    ]

# Generated by Django 2.2.5 on 2019-10-07 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procesamiento_reportes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordeninterna',
            name='fecha_ei',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ordeninterna',
            name='fecha_eri',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ordeninterna',
            name='fecha_lab',
            field=models.DateField(blank=True, null=True),
        ),
    ]

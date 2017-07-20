# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('modelos', '0001_initial'),
        ('estados', '0001_initial'),
        ('instituciones', '0001_initial'),
        ('grados', '0001_initial'),
        ('tipo_educacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=50)),
                ('fecha_s', models.DateField()),
                ('fecha_e', models.DateField()),
                ('serial', models.CharField(max_length=100)),
                ('status', models.CharField(blank=True, max_length=1, null=True, choices=[(b'1', b'Atendiendo'), (b'2', b'Remitida'), (b'3', b'Reparada'), (b'4', b'Entregada'), (b'5', b'Devuelta')])),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('sexo', models.CharField(default=0, max_length=1, choices=[(b'0', b'Seleccione'), (b'1', b'Femenino'), (b'2', b'Masculino')])),
                ('edad', models.IntegerField()),
                ('escuela', models.CharField(max_length=50)),
                ('parroquia', models.IntegerField()),
                ('municipio', models.IntegerField()),
                ('direcc_es', models.TextField(null=True, blank=True)),
                ('cedula', models.IntegerField()),
                ('nombre2', models.CharField(max_length=50)),
                ('apellido2', models.CharField(max_length=50)),
                ('telefono1', models.CharField(max_length=50)),
                ('telefono2', models.CharField(max_length=50, null=True, blank=True)),
                ('email', models.CharField(max_length=100)),
                ('municipio2', models.IntegerField()),
                ('parroquia2', models.IntegerField()),
                ('direcc_re', models.TextField(null=True, blank=True)),
                ('portatil', models.BooleanField(default=False)),
                ('contrato', models.BooleanField(default=False)),
                ('bateria', models.BooleanField(default=False)),
                ('caja', models.BooleanField(default=False)),
                ('cargador', models.BooleanField(default=False)),
                ('reparacion', models.TextField(null=True, blank=True)),
                ('estado', models.ForeignKey(related_name='institucion_estado', on_delete=django.db.models.deletion.SET_NULL, to_field=b'cod_estado', to='estados.Estado', null=True)),
                ('estado2', models.ForeignKey(related_name='representante_estado', on_delete=django.db.models.deletion.SET_NULL, to_field=b'cod_estado', to='estados.Estado', null=True)),
                ('grado', models.ForeignKey(related_name='registro_grado', to='grados.Grados', null=True)),
                ('institucion', models.ForeignKey(related_name='registro_institucion', to='instituciones.Institucion', null=True)),
                ('modelo', models.ForeignKey(related_name='computador_modelo', to='modelos.Modelos', null=True)),
                ('tipo', models.ForeignKey(related_name='registro_tipo', to='tipo_educacion.TipoEducacion', null=True)),
                ('user_create', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_update', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

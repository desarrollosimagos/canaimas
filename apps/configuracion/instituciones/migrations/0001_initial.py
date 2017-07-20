# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('estados', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_institucion', models.CharField(unique=True, max_length=100)),
                ('siglas', models.CharField(max_length=15)),
                ('telefono', models.CharField(max_length=11)),
                ('correo', models.CharField(max_length=100, null=True)),
                ('municipio', models.IntegerField(null=True, blank=True)),
                ('parroquia', models.IntegerField(null=True, blank=True)),
                ('direccion', models.CharField(max_length=200)),
                ('institucion_activa', models.BooleanField(default=False)),
                ('fecha_create', models.DateTimeField(auto_now_add=True)),
                ('fecha_update', models.DateTimeField(auto_now=True, null=True)),
                ('estado', models.ForeignKey(related_name='estado_institucion', on_delete=django.db.models.deletion.SET_NULL, to_field=b'cod_estado', blank=True, to='estados.Estado', null=True)),
                ('user_create', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_update', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('nom_institucion',),
            },
            bases=(models.Model,),
        ),
    ]

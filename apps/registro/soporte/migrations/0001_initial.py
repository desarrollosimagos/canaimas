# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('instituciones', '0001_initial'),
        ('modelos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('solicitud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Soporte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serial', models.CharField(max_length=30)),
                ('problema', models.TextField(max_length=300)),
                ('descripcion', models.TextField(max_length=300)),
                ('hardware', models.BooleanField(default=False)),
                ('software', models.BooleanField(default=False)),
                ('status', models.CharField(default=0, max_length=1, choices=[(b'0', b'Seleccione'), (b'2', b'Remitida'), (b'3', b'Reparada')])),
                ('fecha_create', models.DateTimeField(auto_now_add=True)),
                ('fecha_update', models.DateTimeField(auto_now=True, null=True)),
                ('cod_solicitud', models.ForeignKey(to='solicitud.Registros')),
                ('institucion', models.ForeignKey(blank=True, to='instituciones.Institucion', null=True)),
                ('modelo', models.ForeignKey(to='modelos.Modelos')),
                ('user_create', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_update', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('cod_solicitud',),
            },
            bases=(models.Model,),
        ),
    ]

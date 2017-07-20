# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cod_municipio', models.IntegerField(null=True)),
                ('municipio', models.CharField(max_length=50, null=True)),
                ('estado', models.ForeignKey(related_name='estado_municipio', on_delete=django.db.models.deletion.SET_NULL, to_field=b'cod_estado', to='estados.Estado', null=True)),
            ],
            options={
                'ordering': ('estado', 'cod_municipio', 'municipio'),
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='municipio',
            unique_together=set([('estado', 'cod_municipio', 'municipio')]),
        ),
    ]

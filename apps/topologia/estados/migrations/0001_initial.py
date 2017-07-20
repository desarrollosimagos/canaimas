# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cod_estado', models.IntegerField(unique=True, null=True)),
                ('estado', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'ordering': ('cod_estado',),
            },
            bases=(models.Model,),
        ),
    ]

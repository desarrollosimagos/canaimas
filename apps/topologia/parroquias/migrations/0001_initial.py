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
            name='Parroquia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parroquia', models.CharField(max_length=50)),
                ('cod_parroquia', models.IntegerField(null=True)),
                ('municipio', models.IntegerField(null=True)),
                ('estado', models.ForeignKey(related_name='estado_parroquia', on_delete=django.db.models.deletion.SET_NULL, to_field=b'cod_estado', to='estados.Estado', null=True)),
            ],
            options={
                'ordering': ('estado', 'municipio', 'cod_parroquia', 'parroquia'),
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='parroquia',
            unique_together=set([('estado', 'municipio', 'parroquia')]),
        ),
    ]

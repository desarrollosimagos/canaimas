# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tipo_educacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grado', models.CharField(max_length=60)),
                ('tipo', models.ForeignKey(related_name='tipo_grado', to='tipo_educacion.TipoEducacion', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-08 23:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empregado', '0006_auto_20170208_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='estagiario',
            name='inicio_do_contrato',
            field=models.DateField(default='2017-02-08', verbose_name='Início Contrato'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estagiario',
            name='previsao_termino_do_contrato',
            field=models.DateField(default='2017-02-08', verbose_name='Previsão de Termino'),
            preserve_default=False,
        ),
    ]

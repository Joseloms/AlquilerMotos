# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 22:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alquiler', '0005_auto_20171015_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alquiler',
            name='descripcion',
        ),
    ]

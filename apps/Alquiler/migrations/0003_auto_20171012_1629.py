# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 20:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alquiler', '0002_auto_20171012_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alquiler',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-23 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alquiler', '0011_auto_20171020_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='alquiler',
            name='tiempo',
            field=models.CharField(default='fdsfds', max_length=100),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 21:37
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alquiler', '0017_alquiler_total_exceso'),
    ]

    operations = [
        migrations.AddField(
            model_name='alquiler',
            name='total_alquiler',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=20),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0004_auto_20160708_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='nego_factor',
            field=models.DecimalField(decimal_places=2, default=1.05, max_digits=3),
        ),
    ]

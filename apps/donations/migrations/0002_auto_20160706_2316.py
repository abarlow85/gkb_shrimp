# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 23:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bikeoption',
            name='price_factor',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
        migrations.AlterField(
            model_name='brandoption',
            name='price_factor',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
        migrations.AlterField(
            model_name='cosmeticoption',
            name='price_factor',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
        migrations.AlterField(
            model_name='featuresoption',
            name='price_factor',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
        migrations.AlterField(
            model_name='frameoption',
            name='price_factor',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
        migrations.AlterField(
            model_name='wheeloption',
            name='price_factor',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
    ]

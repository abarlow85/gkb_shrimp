# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0003_bike'),
    ]

    operations = [
        migrations.AddField(
            model_name='brandoption',
            name='requisites',
            field=models.ManyToManyField(to='donations.BikeOption'),
        ),
        migrations.AddField(
            model_name='cosmeticoption',
            name='requisites',
            field=models.ManyToManyField(to='donations.BikeOption'),
        ),
        migrations.AddField(
            model_name='featuresoption',
            name='requisites',
            field=models.ManyToManyField(to='donations.BikeOption'),
        ),
        migrations.AddField(
            model_name='frameoption',
            name='requisites',
            field=models.ManyToManyField(to='donations.BikeOption'),
        ),
        migrations.AddField(
            model_name='wheeloption',
            name='requisites',
            field=models.ManyToManyField(to='donations.BikeOption'),
        ),
        migrations.AlterField(
            model_name='bike',
            name='bike_features',
            field=models.ManyToManyField(blank=True, to='donations.FeaturesOption'),
        ),
        migrations.AlterField(
            model_name='bikeoption',
            name='price_factor',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='brandoption',
            name='price_factor',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='cosmeticoption',
            name='price_factor',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='featuresoption',
            name='price_factor',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='frameoption',
            name='price_factor',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='wheeloption',
            name='price_factor',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
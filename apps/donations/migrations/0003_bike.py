# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 23:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0002_auto_20160706_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bike_price', models.DecimalField(decimal_places=2, default=200.0, max_digits=6)),
                ('bike_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donations.BrandOption')),
                ('bike_cosmetic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donations.CosmeticOption')),
                ('bike_features', models.ManyToManyField(to='donations.FeaturesOption')),
                ('bike_frame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donations.FrameOption')),
                ('bike_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donations.BikeOption')),
                ('bike_wheel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donations.WheelOption')),
            ],
        ),
    ]

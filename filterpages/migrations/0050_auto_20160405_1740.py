# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-05 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filterpages', '0049_auto_20160405_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='make',
            field=models.CharField(blank=True, choices=[('Mitsubishi', 'Mitsubishi'), ('smart', 'smart'), ('Chevrolet', 'Chevrolet'), ('Volkswagen', 'Volkswagen'), ('Nissan', 'Nissan'), ('Ford', 'Ford'), ('FIAT', 'FIAT'), ('Kia', 'Kia'), ('Mercedes-Benz', 'Mercedes-Benz'), ('BMW', 'BMW'), ('Tesla', 'Tesla')], max_length=60),
        ),
    ]
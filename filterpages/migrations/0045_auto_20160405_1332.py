# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-05 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filterpages', '0044_auto_20160405_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='drive',
            field=models.CharField(blank=True, choices=[('front-wheel drive', 'front-wheel drive'), ('rear-wheel drive', 'rear-wheel drive'), ('all-wheel drive', 'rear-wheel drive')], max_length=60),
        ),
    ]

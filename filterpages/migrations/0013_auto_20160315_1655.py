# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-15 20:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filterpages', '0012_auto_20160315_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='city_mpg',
            field=models.PositiveSmallIntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='hwy_mpg',
            field=models.PositiveSmallIntegerField(default=None),
        ),
    ]

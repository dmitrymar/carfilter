# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-16 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filterpages', '0027_auto_20160316_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='battery',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
    ]

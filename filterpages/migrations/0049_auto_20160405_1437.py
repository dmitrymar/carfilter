# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-05 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filterpages', '0048_carmodel_display'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='make',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]

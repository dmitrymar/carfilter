# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-16 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filterpages', '0017_carmodel_range'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='battery',
            field=models.CommaSeparatedIntegerField(blank=True, max_length=1, null=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-16 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filterpages', '0032_auto_20160316_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='version',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]

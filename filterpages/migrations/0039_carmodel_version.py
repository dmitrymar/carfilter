# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-16 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filterpages', '0038_remove_carmodel_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='version',
            field=models.CharField(max_length=60, null=True),
        ),
    ]

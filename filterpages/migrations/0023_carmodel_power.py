# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-16 18:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filterpages', '0022_carmodel_motor'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='power',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
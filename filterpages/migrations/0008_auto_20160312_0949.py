# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-12 14:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filterpages', '0007_carmodel_body_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmodel',
            old_name='body_type',
            new_name='body',
        ),
    ]

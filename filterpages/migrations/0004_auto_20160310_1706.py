# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-10 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filterpages', '0003_auto_20160310_1613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmodel',
            old_name='lowest_price_view',
            new_name='lowest_price',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='detail_url',
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='image_url',
            field=models.FilePathField(max_length=200, path=None),
        ),
    ]
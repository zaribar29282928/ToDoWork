# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-10 12:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0005_auto_20171010_1541'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todowork',
            old_name='data_end',
            new_name='date_end',
        ),
        migrations.RenameField(
            model_name='todowork',
            old_name='data_start',
            new_name='date_start',
        ),
    ]

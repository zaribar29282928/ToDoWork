# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-11 14:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0006_auto_20171010_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todowork',
            name='tapStatus',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-05 22:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0010_activity_imageadd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='imageadd',
        ),
    ]
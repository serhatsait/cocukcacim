# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-22 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0004_auto_20180119_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='event_date',
            field=models.DateField(blank=True, null=True, verbose_name='Etkinlik Tarihi'),
        ),
    ]
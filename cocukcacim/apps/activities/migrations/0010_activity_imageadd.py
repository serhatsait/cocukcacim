# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-05 22:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0009_auto_20180205_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='imageadd',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Görsel ekle'),
        ),
    ]
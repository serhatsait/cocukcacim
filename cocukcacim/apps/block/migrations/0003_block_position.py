# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 21:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0002_block_description_align'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='block.BlockPosition', verbose_name='Blok Pozisyonu'),
        ),
    ]

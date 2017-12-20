# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-20 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturuldu')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellendi')),
                ('event_date', models.DateTimeField(verbose_name='Etkinlik Tarihi')),
                ('title', models.CharField(max_length=255, verbose_name='Başlık')),
                ('description', models.TextField(blank=True, verbose_name='Açıklama')),
            ],
            options={
                'verbose_name': 'Etkinlik',
                'verbose_name_plural': 'Etkinlikler',
                'ordering': ['-created_at'],
            },
        ),
    ]
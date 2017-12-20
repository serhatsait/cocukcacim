# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-20 18:03
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturuldu')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellendi')),
                ('order', models.IntegerField(verbose_name='Sıra')),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='featured_images/', verbose_name='Öne Çıkan Resim')),
                ('body_image', models.ImageField(blank=True, null=True, upload_to='featured_images/', verbose_name='Body Background Resim')),
                ('title', models.CharField(default='', max_length=255, verbose_name='Başlık')),
                ('context', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='İçerik')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_pages', to='page.Page', verbose_name='Üst Sayfa')),
            ],
            options={
                'verbose_name': 'Sabit Sayfa',
                'verbose_name_plural': 'Sabit Sayfalar',
                'ordering': ['parent__id', 'order'],
            },
        ),
    ]
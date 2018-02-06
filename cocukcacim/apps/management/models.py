# -*- coding: utf-8 -*-
from django.db import models


class Whoarewe(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturuldu")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncellendi")
    image = models.ImageField(verbose_name="Biz kimiz? logo")
    text = models.TextField(verbose_name="Biz kimiz? açıklama")

    class Meta:
        verbose_name = "Biz kimiz?"
        verbose_name_plural = "Biz kimiz içeriği"


class Whatwedo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturuldu")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncellendi")
    text1bar = models.CharField(max_length=225, verbose_name="Ne yapıyoruz bar 1. kısım")
    textbar1 = models.TextField(verbose_name="Ne yapıyoruz bar 1. kısım içeriği")
    text2bar = models.CharField(max_length=225, verbose_name="Ne yapıyoruz bar 2. kısım")
    textbar2 = models.TextField(verbose_name="Ne yapıyoruz bar 2. kısım içeriği")
    text3bar = models.CharField(max_length=225, verbose_name="Ne yapıyoruz bar 3. kısım")
    textbar3 = models.TextField(verbose_name="Ne yapıyoruz bar 3. kısım içeriği")

    class Meta:
        verbose_name = "Ne yapıyoruz?"
        verbose_name_plural = "Ne yapıyoruz içeriği"


class Managemembers(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturuldu")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncellendi")
    member = models.CharField(max_length=225, verbose_name="Üye ismi")
    member_appellation = models.CharField(max_length=225, verbose_name="Üye ünvanı")
    member_bio = models.TextField(verbose_name="Üye özgeçmişi")
    member_photo = models.ImageField(verbose_name="Üye fotoğrafı")

    class Meta:
        verbose_name = "üye"
        verbose_name_plural = "Yönetim Kurulu"

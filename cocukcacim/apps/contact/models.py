from django.db import models


class Contactpage(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturuldu")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncellendi")
    adress = models.TextField(verbose_name="Adres", default="Boğazkent Mah. 91.Sk. Kapı No:9/3 Serik/ANTALYA")
    phone1 = models.CharField(max_length=225, verbose_name="Telefon 1", default="+90 541 722 13 75")
    phone2 = models.CharField(max_length=225, verbose_name="Telefon 2", default="+90 544 802 06 00")
    email = models.CharField(max_length=225, verbose_name="E-posta", default="info@cocukcacim.org")
    facebook = models.CharField(max_length=225, verbose_name="Facebook adresi", default="https://www.facebook.com/cocukcacim")
    twitter = models.CharField(max_length=225, verbose_name="Twitter adresi", default="https://twitter.com/cocukcacim")
    instagram = models.CharField(max_length=225, verbose_name="İnstagram adresi", default="https://www.instagram.com/cocukcacim/")

    class Meta:
        verbose_name = "İletişim"
        verbose_name_plural = "İletişim Detayları"

    def __str__(self):
        return self.adress

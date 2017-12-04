from django.db import models


class BlockPosition(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncelleme Tarihi")
    name = models.CharField(max_length=255, verbose_name="Pozisyon İsmi")
    position_name_slug = models.CharField(max_length=60, verbose_name="Pozisyon IDsi")

    # Primary Key veya ID

    # Sınıfla ilgili bilgiler
    class Meta:
        verbose_name = "Blok Pozisyonu"
        verbose_name_plural = "Blok Pozisyonları"
        ordering = ['created_at']

    # classın override ettiğimiz fonksiyonları
    def __str__(self):
        return self.name


class Block(models.Model):
    ALIGN = (
        ('LEFT', 'LEFT'),
        ('CENTER', 'CENTER'),
        ('RIGHT', 'RIGHT'),
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncelleme Tarihi")
    name = models.CharField(max_length=255, verbose_name="İsim", default="Blok İsmi Giriniz!!!!")
    title1 = models.CharField(max_length=255, verbose_name="Başlık 1", blank=True, null=True)
    title2 = models.CharField(max_length=255, verbose_name="Başlık 2", blank=True, null=True)
    icon = models.CharField(max_length=255, verbose_name="Font Awesome Icon İsmi", blank=True, null=True)
    description = models.TextField(verbose_name="Açıklama", null=True, blank=True)
    description_align = models.CharField(max_length=255, choices=ALIGN, verbose_name="Açıklama Hizalama", blank=True)

    image1 = models.TextField(verbose_name="Resim 1", null=True, blank=True)
    image2 = models.TextField(verbose_name="Resim 2", blank=True, null=True)
    position = models.ForeignKey(BlockPosition, null=True, blank=True, verbose_name="Blok Pozisyonu")

    # Sınıfla ilgili bilgiler
    class Meta:
        verbose_name = "Blok"
        verbose_name_plural = "Bloklar"
        ordering = ['created_at']

    # classın override ettiğimiz fonksiyonları
    def __str__(self):
        return self.title1

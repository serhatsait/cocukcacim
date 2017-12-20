from django.db import models


class Activity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturuldu")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncellendi")
    event_date = models.DateTimeField(verbose_name="Etkinlik Tarihi")
    title = models.CharField(max_length=255, verbose_name="Başlık")
    description = models.TextField(verbose_name="Açıklama", blank=True)

    class Meta:
        verbose_name = "Etkinlik"
        verbose_name_plural = "Etkinlikler"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

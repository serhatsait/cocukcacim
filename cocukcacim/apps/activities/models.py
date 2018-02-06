from django.db import models


class Activity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturuldu")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncellendi")
    event_date = models.DateField(verbose_name="Etkinlik Tarihi",blank=True,null=True)
    title = models.CharField(max_length=255, verbose_name="Başlık")
    description = models.TextField(verbose_name="Açıklama", blank=True,null=True)
    image = models.ImageField(verbose_name="Etkinlik Resmi",default="Boş")

    class Meta:
        verbose_name = "Etkinlik"
        verbose_name_plural = "Etkinlikler"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class EventActivity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturuldu")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncellendi")
    title = models.CharField(max_length=255, verbose_name="Başlık",blank=True,null=True)
    event = models.ForeignKey('activities.Activity', related_name='activities', on_delete=models.CASCADE, verbose_name="Etkinlik")
    image = models.ImageField(upload_to='event-activity-images', verbose_name="Görsel",blank=True,null=True)

    class Meta:
        verbose_name = "Etkinlik Resimleri"
        verbose_name_plural = "Etkinlik Resimleri"
        ordering = ['event']

    def __str__(self):
        return self.title


from django.db import models
from django.core.urlresolvers import reverse
from unicode_tr.extras import slugify
from ckeditor_uploader.fields import RichTextUploadingField


class Page(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturuldu")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncellendi")
    parent = models.ForeignKey('page.Page', related_name='sub_pages', null=True, blank=True,
                               limit_choices_to={'parent__parent__isnull': True}, verbose_name="Üst Sayfa")
    order = models.IntegerField(verbose_name="Sıra")
    featured_image = models.ImageField(upload_to="featured_images/", null=True, blank=True,
                                       verbose_name="Öne Çıkan Resim")
    body_image = models.ImageField(upload_to="featured_images/", null=True, blank=True,
                                   verbose_name="Body Background Resim")
    title = models.CharField(max_length=255, verbose_name="Başlık", default="")
    context = RichTextUploadingField(blank=True, verbose_name="İçerik")

    class Meta:
        verbose_name = "Sabit Sayfa"
        verbose_name_plural = "Sabit Sayfalar"
        ordering = ['parent__id', 'order']

    def __str__(self):
        return self.get_title()

    def get_title(self):
        return getattr(self, 'title')

    get_title.short_description = "Title"

    def get_context(self):
        return getattr(self, 'context')

    get_context.short_description = "İçerik"

    def get_absolute_url(self):
        return reverse('page:page', kwargs={'page_id': self.id, 'page_slug': slugify(self.get_title())})

from django.contrib import admin
from cocukcacim.apps.page.models import Page


# admin: Page
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'order', 'created_at', 'updated_at')
    list_filter = ('parent', 'created_at', 'updated_at')
    search_fields = ('title', 'context', 'created_at', 'updated_at')


admin.site.register(Page, PageAdmin)

from django.contrib import admin
from cocukcacim.apps.activities.models import Activity, EventActivity


class EventActivityInline(admin.StackedInline):
    model = EventActivity


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    inlines = [
        EventActivityInline,
    ]


admin.site.register(Activity, EventAdmin)

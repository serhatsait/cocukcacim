from django.contrib import admin
from cocukcacim.apps.block.models import BlockPosition, Block

admin.site.register(BlockPosition)


class BlockAdmin(admin.ModelAdmin):
    list_display = ('title1', 'name', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'title1', 'name')
    search_fields = ('title1', 'title2', 'name',)


admin.site.register(Block, BlockAdmin)

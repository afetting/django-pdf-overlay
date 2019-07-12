from django.contrib import admin

from .models import PDF


def regenerate_layout_images(modeladmin, request, queryset):
    for item in queryset:  # type: PDF
        item.generate_page_layout_images()
regenerate_layout_images.short_description = 'Regenerate Layout Images'


@admin.register(PDF)
class PDFAdmin(admin.ModelAdmin):
    list_display = ['name', 'file', 'page_count']

    actions = [regenerate_layout_images]

    def page_count(self, obj):
        return obj.pages.count()
    page_count.short_description = 'Page Count'

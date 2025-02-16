from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin

from .models import Location, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image

    readonly_fields = ["image_preview"]
    extra = 1
    fields = ["image", "location", "image_preview", "number"]
    ordering = ["number"]
    sortable_field_name = "number"

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
        return "(No image)"


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(Image)

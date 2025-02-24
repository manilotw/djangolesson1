from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin

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
            return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />', obj.image.url)
        return "(No image)"


@admin.register(Location)
class LocationAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["id",
                    "image_preview",
                    "location"]
    
    search_fields = ["location__title"]
    list_filter = ["location"]
    raw_id_fields = ["location"]  

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />', obj.image.url)
        return "(No image)"

    image_preview.short_description = "Preview"

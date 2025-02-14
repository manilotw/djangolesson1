from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.

from .models import Location, Image

class ImageInline(admin.TabularInline):
    model = Image

    readonly_fields = ["image"]

    readonly_fields = ["image_preview"]

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')
        return "(No image)"

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Image)
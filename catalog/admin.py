from django.contrib import admin

# Register your models here.

from .models import Location, Image

class ImageInline(admin.TabularInline):
    model = Image

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Image)
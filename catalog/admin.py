from django.contrib import admin

# Register your models here.

from .models import Location, Image

admin.site.register(Location)
admin.site.register(Image)
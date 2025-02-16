from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from catalog.views import show_map, place

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_map),
    path('tinymce/', include('tinymce.urls')),
    path('places/<int:place_id>', place, name='get_place')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

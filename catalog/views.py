import json

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse

from catalog.models import Location


def show_map(request):
    locations = Location.objects.all()

    features = [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [location.lng, location.lat],
            },
            "properties": {
                "title": location.title,
                "placeId": location.id,
                "detailsUrl": reverse("get_place", kwargs={"place_id": location.id}),
            },
        }
        for location in locations
    ]

    locations_geojson = {
        "type": "FeatureCollection",
        "features": features,
    }

    return render(request, "index.html", locations_geojson)


def place(request, place_id):
    location = get_object_or_404(Location.objects.prefetch_related('imgs'), id=place_id)

    place = {
        "title": location.title,
        "imgs": [str(img.image.url) for img in location.imgs.all()],
        "description_short": location.short_description,
        "description_long": location.long_description,
        "coordinates": {
            "lat": location.lat,
            "lng": location.lng,
        },
    }

    return JsonResponse(
        place,
        safe=False,
        json_dumps_params={
            "indent": 2,
            "ensure_ascii": False
        },
    )

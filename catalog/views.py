import json
from django.shortcuts import render, get_object_or_404
from catalog.models import Location
from django.http import HttpResponse, JsonResponse
from where_to_go import settings
from django.urls import reverse

def show_map(request):

    locations = Location.objects.all()

    features = []

    for location in locations:

        feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [location.lng, location.lat]
                },
                "properties": {
                    "title": location.title,
                    "placeId": location.id,
                    "detailsUrl": reverse(
                                        'get_place',
                                        kwargs={'place_id': location.id}
                                                )
                }
            }
        features.append(feature)
    
    locations_geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    context = {
        'locations_json': json.dumps(locations_geojson)
    }

    return render(request, "index.html", context)


def place(request, place_id):

    location = get_object_or_404(Location, id=place_id)

    place = {
    "title": location.title,
    "imgs": [],
    "description_short": location.description_short,
    "description_long": location.description_long,
    "coordinates": {
        "lat": location.lat,
        "lng": location.lng
    }
}
    for img in location.img.all():
        place['imgs'].append(str(img.image.url))


    return JsonResponse(place, safe=False, json_dumps_params={'indent': 2, 'ensure_ascii': False})
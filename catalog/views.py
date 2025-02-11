import json
from django.shortcuts import render
from catalog.models import Location

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
                    "detailsUrl": "/static/places/moscow_legends.json"
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
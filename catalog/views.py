import json
from django.shortcuts import render
from catalog.models import Location

def show_map(request):
    locations = [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [37.62, 55.793676]
            },
            "properties": {
                "title": "«Легенды Москвы",
                "placeId": "moscow_legends",
                "detailsUrl": "/static/places/moscow_legends.json"
            }
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [37.64, 55.753676]
            },
            "properties": {
                "title": "Крыши24.рф",
                "placeId": "roofs24",
                "detailsUrl": "/static/places/roofs24.json"
            }
        },
    ]

    context = {
        'locations_json': json.dumps(locations)
    }
    return render(request, "index.html", context)
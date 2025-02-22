import os
import requests
import time
import sys

from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile

from catalog.models import Image, Location


class Command(BaseCommand):
    help = "Загрузка данных с JSON"

    def add_arguments(self, parser):
        parser.add_argument(
            "data_url",
            type=str,
            help="Введите ссылку на JSON"
        )

    def handle(self, *args, **kwargs):
        def upload_image(place, image_url):
            try:
                response = requests.get(image_url)
                response.raise_for_status()
                image_name = os.path.basename(image_url)
                Image.objects.create(
                    location=place,
                    image=ContentFile(response.content, name=image_name),
                )
            except requests.exceptions.HTTPError as err:
                print(f"Ошибка HTTP при загрузке {image_url}: {err}", file=sys.stderr)
            except requests.exceptions.ConnectionError:
                print(f"Проблемы с сетью при загрузке {image_url}. Повтор через 5 секунд.", file=sys.stderr)
                time.sleep(5)
                upload_image(place, image_url)

        url = kwargs["data_url"]
        response = requests.get(url)
        response.raise_for_status()
        answer = response.json()

        title = answer["title"]
        images_url = answer["imgs"]
        description_short = answer["description_short"]
        description_long = answer["description_long"]
        lng = answer["coordinates"]["lng"]
        lat = answer["coordinates"]["lat"]

        place, created = Location.objects.get_or_create(
            title=title,
            lat=lat,
            lng=lng,
            defaults={
                "short_description": description_short,
                "long_description": description_long,
            },
        )

        for image_url in images_url:
            upload_image(place, image_url)

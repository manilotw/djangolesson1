from django.db import models
from tinymce.models import HTMLField

class Location(models.Model):
    title = models.CharField('Название локаций', max_length=200)
    short_description = models.TextField('Короткое описание', blank=True)
    long_description = HTMLField('Длинное описание', blank=True)
    lat = models.FloatField('Широта')
    lng = models.FloatField('Долгота')

    def __str__(self):
        return self.title
    
class Image(models.Model):
    location = models.ForeignKey(Location,default=0, on_delete=models.CASCADE, related_name='imgs')
    number = models.IntegerField('Номер для порядка', default=0, blank=True)
    image = models.ImageField('Фотография')

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f"{self.number} {self.location.title}"




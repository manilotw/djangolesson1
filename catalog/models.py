from django.db import models

# Create your models here.

class Location(models.Model):
    title = models.CharField('Название локаций', max_length=200)
    description_short = models.TextField('Короткое описание')
    description_long = models.TextField('Длинное описание')
    lng = models.FloatField('Координация 1')
    lat = models.FloatField('Координация 2')

    def __str__(self):
        return self.title
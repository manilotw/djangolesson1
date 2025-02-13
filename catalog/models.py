from django.db import models

# Create your models here.

class Location(models.Model):
    title = models.CharField('Название локаций', max_length=200)
    description_short = models.TextField('Короткое описание')
    description_long = models.TextField('Длинное описание')
    lat = models.FloatField('Координация 1')
    lng = models.FloatField('Координация 2')

    def __str__(self):
        return self.title
    
class Image(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='img')
    number = models.IntegerField('Номер для порядка')
    image = models.ImageField('Фотография')

    def __str__(self):
        return f"{self.number}, {self.location.title}"




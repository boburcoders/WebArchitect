from django.db import models

# Create your models here.

from django.db import models


# Create your models here.
class WeatherData(models.Model):
    id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=30)
    pressure = models.FloatField()
    temperature = models.FloatField()
    description = models.CharField(max_length=40)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.city_name



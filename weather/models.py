from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Country(models.Model):
    code = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
      verbose_name_plural = "countries"

    def __str__(self):
        return self.name

class City(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    class Meta:
      verbose_name_plural = "cities"

    def __str__(self):
        return self.name
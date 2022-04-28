from django.db import models

# Create your models here.
class Shoe(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    size =  models.DecimalField(max_digits = 3, decimal_places = 1)
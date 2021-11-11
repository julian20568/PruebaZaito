from django.db import models

# Create your models here.

class Productos(models.Model):
    cod = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    stock = models.IntegerField(blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    #price = models.DecimalField(max_digits = 30, decimal_places = 2)
    paused = models.BooleanField(blank=False)
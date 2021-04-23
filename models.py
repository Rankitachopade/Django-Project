from django.db import models

# Create your models here.

class Quiz(models.Model):
 name = models.CharField(max_length=255)
 price = models.FloatField()
 image = models.CharField(max_length=255)

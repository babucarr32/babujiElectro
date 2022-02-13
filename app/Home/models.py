from django.db import models
from .models import models

class homeModel(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    detail = models.TextField( default= "")

    def __str__(self):
        return self.name
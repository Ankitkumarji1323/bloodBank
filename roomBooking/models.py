from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = BooleanField(default=False)


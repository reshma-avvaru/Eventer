from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
# Create your models here.

class Address(models.Model):
    address1 = models.CharField("Address line 1", max_length=1024)
    address2 = models.CharField("Address line 2", max_length=1024, blank=True, null=True)
    zip_code = models.CharField("ZIP", max_length=12)
    city = models.CharField("City", max_length=1024)

class Event(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateField()
    time=models.TimeField()
    location=models.ForeignKey(Address, on_delete=CASCADE)
    is_liked=models.BooleanField(default=False)
    image=models.ImageField(upload_to='images/')
    description=CharField(max_length=255)



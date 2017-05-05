from django.db import models
from mongoengine import *

class Store(Document):
    name = StringField(max_length=200)
    address = StringField(max_length=500)
    latitude = FloatField(max_digits=15, decimal_places=10)
    longitude = FloatField(max_digits=15, decimal_places=10)




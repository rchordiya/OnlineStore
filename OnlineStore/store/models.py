from django.db import models
from mongoengine import *

class Store(Document):
    name = StringField(max_length=200)
    address = StringField(max_length=500)
    latitude = DecimalField(max_digits=9, decimal_places=6)
    longitude = DecimalField(max_digits=9, decimal_places=6)
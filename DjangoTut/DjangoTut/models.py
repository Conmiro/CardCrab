
from django.db import models


class Car(models.Model):
    make = models.TextField()
    model = models.TextField()
    year = models.TextField()

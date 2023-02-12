from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
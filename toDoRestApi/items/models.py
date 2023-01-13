from django.db import models

# Create your models here.

class Items(models.Model):
    text = models.CharField(max_length=200, blank=False, default='')
    day = models.CharField(max_length=200, blank=True, default='')
    reminder = models.BooleanField(default=False)
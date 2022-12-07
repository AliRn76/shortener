from django.db import models


class Url(models.Model):
    original = models.CharField(max_length=63)
    shortened = models.CharField(max_length=511)

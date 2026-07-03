from django.db import models

class Fact(models.Model):
    fact = models.CharField(max_length=255)
    liked = models.BooleanField(default=False)

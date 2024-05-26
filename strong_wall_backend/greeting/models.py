from django.db import models


class GreetingModel(models.Model):
    name = models.CharField(max_length=50, default='')

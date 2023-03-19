from django.db import models


# Create your models here.
class Legislation(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    description = models.TextField()


def __str__(self):
    return self.title + '-' + self.url

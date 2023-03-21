from django.db import models


# Create your models here.
class Legislation(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    description = models.TextField()
    def __str__(this):
        return this.title


class Questionanswer(models.Model):
    question = models.TextField()
    answer = models.TextField()
    keywords = models.TextField()
    keyphrase = models.TextField()
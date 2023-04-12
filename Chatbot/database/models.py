from django.db import models


# Create your models here.
class Legislation(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    details = models.TextField()


    def __str__(this):
        return this.title


class Questionanswer(models.Model):
    question = models.TextField()
    answer = models.TextField()
    keywords = models.TextField()
    keyphrase = models.TextField()

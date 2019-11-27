from django.db import models


class Noticia(models.Model):
    link = models.CharField(max_length=200, null=True)
    summary = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)
    image = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title
from django.db import models


class Brazilian(models.Model):
    name = models.CharField(max_length=50, primary_key=True, default="")
    score = models.IntegerField(null=True)
    games = models.IntegerField(null=True)
    wins = models.IntegerField(null=True)
    draws = models.IntegerField(null=True)
    loses = models.IntegerField(null=True)

    def __str__(self):
        return self.name
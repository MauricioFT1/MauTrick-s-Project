from django.db import models
from django.db.models.fields import DateTimeField


class Team(models.Model):
    name = models.CharField(max_length=50, null=True)
    stadium = models.CharField(max_length=50, null=True)
    coach = models.OneToOneField('People', on_delete=models.CASCADE, null=True)
    foundation = models.CharField(max_length=50, null=True)
    # president = models.OneToOneField('People', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
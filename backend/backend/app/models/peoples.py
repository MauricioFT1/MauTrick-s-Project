from django.db import models
from django.db.models.fields import IntegerField , DateField

class People(models.Model):
    birth = models.DateField()
    name = models.CharField(max_length=50)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'People'
        verbose_name_plural = 'Peoples'


    
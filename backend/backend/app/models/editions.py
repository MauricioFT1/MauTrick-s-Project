from django.db import models
from django.db.models.fields import IntegerField , DateField

class Edition(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    participants = models.ManyToManyField("Team")
    number = models.IntegerField(null=True)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Edition'
        verbose_name_plural = 'Editions'

    @property
    def date(self):
        return 'Data: ' + self.date

    
from django.db import models
from django.db.models.fields import IntegerField , DateField

class Edition(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(null=False)
    number = models.IntegerField(null=True)
    participants = models.ManyToManyField("Team")
    

    def __str__(self):
        return 'ID: [{}] - Data: [{}]'.format(self.id, self.date)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Edition'
        verbose_name_plural = 'Editions'

    

    
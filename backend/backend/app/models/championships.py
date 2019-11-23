from django.db import models
from django.db.models.fields import DateField

from . import Team, Edition

ROLE_CHAMPIONSHIP = [
    (0, 'Nacional'),
    (1, 'Internacional')
]

class Championship(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateField()
    role = models.IntegerField(choices=ROLE_CHAMPIONSHIP, default=0)
    editions = models.ManyToManyField(
        'Edition',
        through='EditionChampionship'
    )

    def __str__(self):
        return self.name

class EditionChampionship(models.Model):
    championship = models.ForeignKey(
        'Championship',
        on_delete=models.CASCADE,
    )
    edition = models.ForeignKey(
        'Edition',
        on_delete=models.CASCADE,
    )
    # Se quiser adicionar alguma coisa aqui...

    def __str__(self):
        return str((self.championship, self.edition))

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'EditionChampionship'
        verbose_name_plural = 'EditionChampionships'
from django.contrib import admin

from .models import EditionChampionship, Team, Edition, Championship, People, Noticia, Brazilian

admin.site.register(Edition)
admin.site.register(Team)
admin.site.register(EditionChampionship)
admin.site.register(Championship)
admin.site.register(People)
admin.site.register(Noticia)
admin.site.register(Brazilian)
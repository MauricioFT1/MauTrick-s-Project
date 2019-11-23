from django.conf.urls import url

from .views import (
    ChampionshipCreate, ChampionshipDestroy, ChampionshipGet, ChampionshipList, ChampionshipUpdate,
    PeopleList, TeamList, EditionList
)

urlpatterns = [
    url(r'championships/$', ChampionshipList.as_view()),
    url(r'championships/(?P<pk>\d+)/$', ChampionshipDestroy.as_view()),
    url(r'championships/add/$', ChampionshipCreate.as_view()),
    url(r'championships/get/(?P<pk>\d+)/$', ChampionshipGet.as_view()),
    url(r'championships/edit/(?P<pk>\d+)/$', ChampionshipUpdate.as_view()),
    url(r'peoples/$', PeopleList.as_view()),
    url(r'teams/$', TeamList.as_view()),
    url(r'editions/$', EditionList.as_view()
    )

]

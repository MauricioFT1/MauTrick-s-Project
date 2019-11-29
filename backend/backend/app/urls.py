from django.conf.urls import url

from .views import (
    ChampionshipCreate, ChampionshipDestroy, ChampionshipGet, ChampionshipList, ChampionshipUpdate,
    EditionChampionshipList, EditionChampionshipGet,
    PeopleList, PeopleGet,
    TeamList, TeamDestroy, TeamGet, TeamUpdate,
    EditionList, EditionGet,
    NoticiaList,
    BrazilianList
)
from .montaNoticias import montandoNoticias
from .montaTabela import montandoTabela

urlpatterns = [
    url(r'championships/$', ChampionshipList.as_view()),
    url(r'championships/(?P<pk>\d+)/$', ChampionshipDestroy.as_view()),
    url(r'championships/add/$', ChampionshipCreate.as_view()),
    url(r'championships/get/(?P<pk>\d+)/$', ChampionshipGet.as_view()),
    url(r'championships/edit/(?P<pk>\d+)/$', ChampionshipUpdate.as_view()),

    url(r'peoples/$', PeopleList.as_view()),
    url(r'peoples/get/(?P<pk>\d+)/$', PeopleGet.as_view()),

    url(r'teams/$', TeamList.as_view()),
    url(r'teams/(?P<pk>\d+)/$', TeamDestroy.as_view()),
    url(r'teams/get/(?P<pk>\d+)/$', TeamGet.as_view()),
    url(r'teams/edit/(?P<pk>\d+)/$', TeamUpdate.as_view()),

    url(r'editions/$', EditionList.as_view()),
    url(r'editions/get/(?P<pk>\d+)/$', EditionGet.as_view()),

    url(r'editionschamp/$', EditionChampionshipList.as_view()),
    url(r'editionschamp/get/(?P<pk>\d+)/$', EditionChampionshipGet.as_view()),

    url(r'noticiasmontar/$', NoticiaList.as_view(), montandoNoticias()),

    url(r'brasileiraomontar/$', BrazilianList.as_view(), montandoTabela())

]

from rest_framework import generics, permissions

from app.models import Championship, EditionChampionship
from app.serializers import ChampionshipSerializer, EditionChampionshipSerializer


class ChampionshipList(generics.ListAPIView):
    queryset = Championship.objects.all()
    serializer_class = ChampionshipSerializer
    permission_classes = ()


class ChampionshipDestroy(generics.DestroyAPIView):
    queryset = Championship.objects.all()
    serializer_class = ChampionshipSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )


class ChampionshipUpdate(generics.UpdateAPIView):
    queryset = Championship.objects.all()
    serializer_class = ChampionshipSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )


class ChampionshipCreate(generics.CreateAPIView):
    queryset = Championship.objects.all()
    serializer_class = ChampionshipSerializer
    permission_classes = ()


class ChampionshipGet(generics.RetrieveAPIView):
    queryset = Championship.objects.all()
    serializer_class = ChampionshipSerializer
    permission_classes = ()

class EditionChampionshipList(generics.ListAPIView):
    queryset = EditionChampionship.objects.all()
    serializer_class = EditionChampionshipSerializer
    permission_classes = ()

class EditionChampionshipGet(generics.RetrieveAPIView):
    queryset = EditionChampionship.objects.all()
    serializer_class = EditionChampionshipSerializer
    permission_classes = ()
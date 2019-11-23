from rest_framework import generics, permissions

from app.models import Championship
from app.serializers import ChampionshipSerializer


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

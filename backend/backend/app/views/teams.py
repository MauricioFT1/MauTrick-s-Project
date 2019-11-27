from rest_framework import generics, permissions

from app.models import Team
from app.serializers import TeamSerializer


class TeamList(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = ()

class TeamGet(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = ()

class TeamDestroy(generics.DestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

class TeamUpdate(generics.UpdateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )
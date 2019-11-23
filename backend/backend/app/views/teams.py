from rest_framework import generics

from app.models import Team
from app.serializers import TeamSerializer


class TeamList(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = ()

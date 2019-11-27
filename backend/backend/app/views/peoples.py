from rest_framework import generics

from app.models import People
from app.serializers import PeopleSerializer


class PeopleList(generics.ListAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    permission_classes = ()

class PeopleGet(generics.RetrieveAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    permission_classes = ()

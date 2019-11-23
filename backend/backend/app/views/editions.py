from rest_framework import generics

from app.models import Edition
from app.serializers import EditionSerializer


class EditionList(generics.ListAPIView):
    queryset = Edition.objects.all()
    serializer_class = EditionSerializer
    permission_classes = ()

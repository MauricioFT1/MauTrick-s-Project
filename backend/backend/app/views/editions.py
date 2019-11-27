from rest_framework import generics, permissions

from app.models import Edition
from app.serializers import EditionSerializer


class EditionList(generics.ListAPIView):
    queryset = Edition.objects.all()
    serializer_class = EditionSerializer
    permission_classes = ()

class EditionGet(generics.RetrieveAPIView):
    queryset = Edition.objects.all()
    serializer_class = EditionSerializer
    permission_classes = ()

class EditionDestroy(generics.DestroyAPIView):
    queryset = Edition.objects.all()
    serializer_class = EditionSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

class EditionUpdate(generics.UpdateAPIView):
    queryset = Edition.objects.all()
    serializer_class = EditionSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )
from rest_framework import generics

from app.models import Noticia
from app.serializers import NoticiaSerializer


class NoticiaList(generics.ListAPIView):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer
    permission_classes = ()
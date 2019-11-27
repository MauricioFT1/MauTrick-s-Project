from rest_framework import generics

from app.models import Brazilian
from app.serializers import BrazilianSerializer


class BrazilianList(generics.ListAPIView):
    queryset = Brazilian.objects.all()
    serializer_class = BrazilianSerializer
    permission_classes = ()
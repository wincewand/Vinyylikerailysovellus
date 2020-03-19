from rest_framework import viewsets
from .models import Albumi
from .serializers import AlbumiSerializer

class AlbumiViewSet(viewsets.ModelViewSet):
    queryset = Albumi.objects.all()
    serializer_class = AlbumiSerializer
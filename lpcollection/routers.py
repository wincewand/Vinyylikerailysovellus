from rest_framework import routers
from .albumi.viewsets import AlbumiViewSet

router = routers.DefaultRouter()

router.register(r'albumi', AlbumiViewSet)
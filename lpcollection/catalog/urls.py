from django.urls import include, path

from . import views

urlpatterns = [
    path('fetchAll', views.fetchAll, name='fetchAll'),
     path('fetchOne', views.fetchOne, name='fetchOne'),
]
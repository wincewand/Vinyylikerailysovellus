from django.urls import include, path

from . import views

urlpatterns = [
    path('fetchMatching/<str:record_name>', views.fetchMatching, name='fetchMatching'),
]
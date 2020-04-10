from django.urls import include, path

from . import views

urlpatterns = [
    path('createUser/<str:name>/<str:email>/<str:password>', views.createUser, name='createUser'),
    path('logIn/<str:name>/<str:email>/<str:password>', views.login),
]
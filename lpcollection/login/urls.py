from django.urls import include, path

from . import views

urlpatterns = [
    path('addNew/<str:email>/<str:password>', views.addNew, name='addNewUser'),
    path('fetchOne/<str:email>', views.fetchOne, name='fetchOneUser'),
    path('removeOne/<str:email>', views.removeOne, name='removeOneUser'),
]
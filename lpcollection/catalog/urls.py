from django.urls import include, path

from . import views

urlpatterns = [
    path('fetchAll', views.fetchAll, name='fetchAll'),
    path('addNew', views.addNew, name='addNew'),
    path('fetchOne', views.fetchOne, name='fetchOne'),
    path('removeOne/<int:id>', views.removeOne, name='removeOne'),
]
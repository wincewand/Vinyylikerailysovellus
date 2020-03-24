from django.urls import include, path

from . import views

urlpatterns = [
    path('fetchAll', views.fetchAll, name='fetchAll'),
    path('addNew/<str:name>/<str:artist>/<int:year>', views.addNew, name='addNew'),
    path('fetchOne/<str:id>', views.fetchOne, name='fetchOne'),
    path('removeOne/<str:id>', views.removeOne, name='removeOne'),
]
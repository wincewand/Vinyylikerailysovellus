from django.urls import include, path

from . import views

urlpatterns = [
    path('fetchAll/<str:user>', views.fetchAll, name='fetchAll'),
    path('addNew/<str:name>/<str:artist>/<int:year>/<str:user>', views.addNew, name='addNew'),
    path('fetchOne/<str:id>', views.fetchOne, name='fetchOne'),
    path('removeOne/<str:id>', views.removeOne, name='removeOne'),
]
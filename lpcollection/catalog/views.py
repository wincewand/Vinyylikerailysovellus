from django.shortcuts import render
import json
from .models import Album
from django.db import connection
from django.db.utils import OperationalError
from bson import Binary, Code
from bson.json_util import dumps

# Create your views here.

from django.http import HttpResponse

def fetchAll(request):
    # albums = Album.objects.get()
    #response = '{"data":[{ "name": "Title 1", "artist": "Somebody", "year": "1999", "id": 0 },{ "name": "Title 2", "artist": "Somebody else", "year": "2019", "id": 1 }]}'
    #album = Album(name="Title2",artist="Han Swan", year="1997").save()
    # num_posts = Album.objects.count()
    # try:
    #     connection.ensure_connection()
    # except OperationalError:
    #     connected = False
    # else:
    #     connected = True
    data = Album.objects.all().values()
    return HttpResponse(dumps(data))

def addNew(request):
    response = 'New item added'
    return HttpResponse(response)

def removeOne(request, id):
    response = 'Item removed, id: ' + str(id)
    return HttpResponse(response)

def fetchOne(request):
    response = '{"data":[{ "name": "Title 1", "artist": "Somebody","year": "1999", "id": 0 }]}'
    return HttpResponse(response)

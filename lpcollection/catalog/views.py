from django.shortcuts import render
import json
from .models import Album
from django.db import connection
from django.db.utils import OperationalError
from bson import Binary, Code
from bson.json_util import dumps
from django.http import JsonResponse

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

def addNew(request, name, artist, year):
    Album(name=name,artist=artist, year=year).save()
    return HttpResponse("Item added")

def removeOne(request, id):
    Album.objects.filter(_id=id).delete()
    return HttpResponse("Item deleted!")

def fetchOne(request, id):
    album = Album.objects.filter(_id=id).first()
    return HttpResponse('{"data":[{ "name": "' + album.name + '", "artist": "' + album.artist + '", "year": "' + str(album.year) + '"}]}')

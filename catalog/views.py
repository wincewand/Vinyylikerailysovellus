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

def fetchAll(request, user):
    data = Album.objects.filter(user=user).values()
    return HttpResponse(dumps(data))

def addNew(request, name, artist, year, user):
    Album(name=name,artist=artist, year=year, user=user).save()
    return HttpResponse("Item added!")

def removeOne(request, id):
    Album.objects.filter(_id=id).delete()
    return HttpResponse("Item deleted!")

def fetchOne(request, id):
    album = Album.objects.filter(_id=id).first()
    return HttpResponse('{"data":[{ "name": "' + album.name + '", "artist": "' + album.artist + '", "year": "' + str(album.year) + '"}]}')

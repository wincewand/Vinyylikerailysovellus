from django.shortcuts import render

import json

# Create your views here.

from django.http import HttpResponse


def fetchAll(request):
    response = '{"data":[{ "name": "Title 1", "artist": "Somebody", "year": "1999", "id": 0 },{ "name": "Title 2", "artist": "Somebody else", "year": "2019", "id": 1 }]}'
    return HttpResponse(response)

def addNew(request):
    response = 'New item added'
    return HttpResponse(response)

def removeOne(request, id):
    response = 'Item removed, id: ' + str(id)
    return HttpResponse(response)

def fetchOne(request):
    response = '{"data":[{ "name": "Title 1", "artist": "Somebody","year": "1999", "id": 0 }]}'
    return HttpResponse(response)

from django.shortcuts import render
import json

# Create your views here.

from django.http import HttpResponse


def fetchAll(request):
    response = '{"data":[{ "name": "Title 1", "artist": "Somebody" },{ "name": "Title 2", "artist": "Somebody else" }]}'
    return HttpResponse(response)

def fetchOne(request):
    return HttpResponse("You fetched one item from database")

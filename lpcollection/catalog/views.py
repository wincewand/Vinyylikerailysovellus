from django.shortcuts import render
import json

# Create your views here.

from django.http import HttpResponse


def fetchAll(request):
    return HttpResponse("You fetched all items from database")

def fetchOne(request):
    return HttpResponse("You fetched one item from database")

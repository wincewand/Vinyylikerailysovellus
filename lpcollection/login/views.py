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

def addNewUser(request, email, password):
    User(email=email,password=password).save()
    return HttpResponse("Item added")

def removeOneUser(request, id):
    User.objects.filter(_id=id).delete()
    return HttpResponse("Item deleted!")

def fetchOneUser(request, id):
    User = User.objects.filter(_id=id).first()
    return HttpResponse('{"data":[{ "email": "' + user.email + '", "password": "' + user.password + '", "year": "' + '"}]}')
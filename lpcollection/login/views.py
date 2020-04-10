from django.shortcuts import render
import json
from django.db import connection, DatabaseError
from django.db.utils import OperationalError
from bson import Binary, Code
from bson.json_util import dumps
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpRequest, HttpResponse

# Create your views here.

def createUser(request, name, email, password):

    try:
        user = User.objects.create_user(name, email, password)
        user.save()
        return HttpResponse("User added!")
    except:
        return HttpResponse("Name was already taken!")
    
def login(request, name, password):

    user = authenticate(password=password, username=name)
    if user is not None:
        return HttpResponse("true")
    else:
        return HttpResponse("false")

def removeOneUser(request, id):
    User.objects.filter(_id=id).delete()
    return HttpResponse("Item deleted!")

def fetchOneUser(request, id):
    User = User.objects.filter(_id=id).first()
    return HttpResponse('{"data":[{ "email": "' + user.email + '", "password": "' + user.password + '", "year": "' + '"}]}')
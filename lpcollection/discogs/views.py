from django.shortcuts import render
import discogs_client as discogs
from bson import Binary, Code
from bson.json_util import dumps


# Create your views here.

from django.http import HttpResponse


def index(request):
    d = discogs.Client('ExampleApplication/0.1')
    d = discogs.Client('ExampleApplication/0.1', user_token="kjSzomrwGYmaghjNUbTnTCLtEwlpETrtDkLTKAnF")
    results = d.search('Stockholm By Night', type='release')
    print(results.pages)
    sivut = results.pages
    artist = results[0].artists[0]
    nimi = artist.name
    print(artist.name)
    master_release = d.master(120735)

    print(artist.id)
    print(master_release.main_release)
    print(master_release.title)
    print(master_release.tracklist)
    return HttpResponse("Hello, world. You're at the discogs index. Artisti on "+ nimi)

def fetchMatching(request, record_name):
    #d = discogs.Client('ExampleApplication/0.1')
    d = discogs.Client('ExampleApplication/0.1', user_token="kjSzomrwGYmaghjNUbTnTCLtEwlpETrtDkLTKAnF")
    results = d.search(record_name, type='release')
    response = '{"data":[{ "name": "' + results[0].title + '", "artist": "' + results[0].artists[0].name + '", "year": "' + str(results[0].year) + '" }]}'
    return HttpResponse(response)
    



    
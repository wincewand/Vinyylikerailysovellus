from django.shortcuts import render
import discogs_client as discogs


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
    
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from places.geo_json import get_geo_json
from places.models import Place


def index(request: HttpRequest) -> HttpResponse:
    places = Place.objects.iterator()
    context = get_geo_json(places)
    return render(request, 'places/index.html', context={'context': context})

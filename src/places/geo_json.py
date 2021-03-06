from typing import Union

from django.db import models
from django.urls import reverse

from places.models import Place

GeoJsonFeature = dict[str, Union[str, float]]


def _get_get_json_feature(place: Place) -> GeoJsonFeature:
    return {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [
                place.coordinates['lng'],
                place.coordinates['lat'],
            ]
        },
        'properties': {
            'title': place.title,
            'placeId': place.slug,
            'detailsUrl': reverse('place-detail', kwargs={'place_id': place.pk})
        }
    }


def get_geo_json(places: models.QuerySet) -> list[GeoJsonFeature]:
    return {
        'type': 'FeatureCollection',
        'features': [_get_get_json_feature(place) for place in places],
    }

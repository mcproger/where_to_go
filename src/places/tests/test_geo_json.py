from decimal import Decimal

import pytest

from places.geo_json import get_geo_json
from places.models import Place

pytestmark = [pytest.mark.django_db]


@pytest.mark.usefixtures('place')
def test_get_geo_json() -> None:
    assert get_geo_json(Place.objects.all()) == {
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [
                        Decimal('37.0000000000000000'),
                        Decimal('55.0000000000000000'),
                    ],
                },
                'properties': {
                    'title': 'Test place',
                    'placeId': 'test_place_slug',
                    'detailsUrl': './static/places/test_place_slug.json',
                },
            },
        ],
    }

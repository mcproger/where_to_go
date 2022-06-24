from unittest.mock import ANY

import pytest

from places.models import Place

pytestmark = [pytest.mark.django_db]


def test_get_place(place: Place, api_client) -> None:
    response = api_client.get(f'/places/{place.pk}/')

    data = response.json()

    assert data == {
        'title': 'Test place',
        'imgs': [
            ANY,
        ],
        'description_short': 'Short description',
        'description_long': 'Long description',
        'coordinates': {
            'lng': 37.0,
            'lat': 55.0,
        },
    }
    # factory-boy generates a unique url, so we check
    # manually that the url contains the required media path
    assert '/media/places/' in data['imgs'][0]

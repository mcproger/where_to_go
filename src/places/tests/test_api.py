import pytest

from places.models import Place

pytestmark = [pytest.mark.django_db]


def test_get_place(place: Place, api_client) -> None:
    response = api_client.get(f'/places/{place.pk}/')

    assert response.json() == {
        'title': 'Test place',
        'description_short': 'Short description',
        'description_long': 'Long description',
        'coordinates': {
            'lng': 37.0,
            'lat': 55.0,
        },
    }

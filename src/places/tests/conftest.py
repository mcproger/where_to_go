from decimal import Decimal

import pytest

from places.factories import PlaceFactory, PlaceImageFactory
from places.models import Place


@pytest.fixture()
def place() -> Place:
    place = PlaceFactory(
        title='Test place',
        slug='test_place_slug',
        description_short='Short description',
        description_long='Long description',
        latitude=Decimal(55),
        longitude=Decimal(37),
    )
    PlaceImageFactory(
        place=place,
    )
    return place

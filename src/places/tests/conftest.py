from decimal import Decimal

import pytest

from places.factories import PlaceFactory
from places.models import Place


@pytest.fixture()
def place() -> Place:
    return PlaceFactory(
        title='Test place',
        slug='test_place_slug',
        description_short='Short description',
        description_long='Long description',
        latitude=Decimal(55),
        longitude=Decimal(37),
    )

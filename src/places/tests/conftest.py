from decimal import Decimal

import pytest

from places.factories import PlaceFactory
from places.models import Place


@pytest.fixture()
def place() -> Place:
    return PlaceFactory(
        title='Test place',
        slug='test_place_slug',
        latitude=Decimal(55),
        longitude=Decimal(37),
    )

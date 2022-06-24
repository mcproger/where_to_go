import factory
from factory import django

from places.models import Place, PlaceImage


class PlaceFactory(django.DjangoModelFactory):
    class Meta:
        model = Place


class PlaceImageFactory(django.DjangoModelFactory):
    class Meta:
        model = PlaceImage

    place = factory.SubFactory(PlaceFactory)
    image = django.ImageField(filename='example.jpg', color='blue')

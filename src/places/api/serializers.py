from rest_framework import serializers

from places.models import Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        # TODO (mcproger) add images urls here
        fields = [
            'title',
            'description_short',
            'description_long',
            'coordinates',
        ]

from rest_framework import serializers

from places.models import Place


class PlaceSerializer(serializers.ModelSerializer):
    imgs = serializers.SerializerMethodField()

    class Meta:
        model = Place
        fields = [
            'title',
            'imgs',
            'description_short',
            'description_long',
            'coordinates',
        ]

    def get_imgs(self, obj: Place) -> list[str]:
        return [
            image.image.url
            # there won't be N+1 because we work
            # with the single object. However, be careful to reuse this API
            for image in obj.images.iterator()
        ]

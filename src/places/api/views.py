from typing import Any

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from places.api.serializers import PlaceSerializer
from places.models import Place


class PlaceView(APIView):
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        self._object_id = kwargs['place_id']
        instance = self._get_object()

        return Response(PlaceSerializer(instance).data)

    def _get_object(self) -> Place:
        return get_object_or_404(Place, pk=self._object_id)

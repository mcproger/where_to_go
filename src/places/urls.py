from django.urls import path

from places import views
from places.api import views as api_views

urlpatterns = [
    path('', views.index, name='index'),
    path('places/<int:place_id>/', api_views.PlaceView.as_view()),
]

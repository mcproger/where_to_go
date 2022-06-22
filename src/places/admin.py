from app.admin import admin, ModelAdmin
from places.models import Place


@admin.register(Place)
class PlaceAdmin(ModelAdmin):
    pass

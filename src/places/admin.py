from app.admin import ModelAdmin, admin
from places.models import Place


@admin.register(Place)
class PlaceAdmin(ModelAdmin):
    pass

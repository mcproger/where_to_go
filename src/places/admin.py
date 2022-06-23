from app.admin import ModelAdmin, admin
from places.models import Place, PlaceImage


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 3


@admin.register(PlaceImage)
class PlaceImageAdmin(ModelAdmin):
    pass


@admin.register(Place)
class PlaceAdmin(ModelAdmin):
    inlines = [
        PlaceImageInline,
    ]

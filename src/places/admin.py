from django.http.request import HttpRequest
from django.utils.safestring import mark_safe

from app.admin import ModelAdmin, admin
from app.models import models
from places.models import Place, PlaceImage


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 3
    fields = [
        'title',
        'render_image',
        'order',
    ]
    readonly_fields = [
        'render_image',
    ]

    def render_image(self, obj):
        return mark_safe(
            f'<img src="{obj.image.url}" height="200px" />'
        )


@admin.register(PlaceImage)
class PlaceImageAdmin(ModelAdmin):
    pass


@admin.register(Place)
class PlaceAdmin(ModelAdmin):
    inlines = [
        PlaceImageInline,
    ]

    def get_queryset(self, request: HttpRequest) -> models.QuerySet:
        queryset = super().get_queryset(request)
        return queryset.prefetch_related('images')

from tabnanny import verbose
from django.utils.translation import gettext_lazy as _

from app.models import Model, models


class Place(Model):
    title = models.CharField(_('Title'), max_length=32, db_index=True)
    description_short = models.CharField(_('Short description of the place'), max_length=250, blank=True, null=True)
    description_long = models.TextField(_('Detailed description of the place'), blank=True, null=True)

    class Meta:
        verbose_name = _('Place')
        verbose_name_plural = _('Places')

    def __str__(self) -> str:
        return self.title


class PlaceImage(Model):
    title = models.CharField(_('Title'), max_length=32, db_index=True)
    order = models.PositiveIntegerField(_('Image order'), default=0)
    image = models.ImageField(
        _('The place image'),
        upload_to='places',
        help_text=_('Don\'t forget to specify the order of the picture'),
    )

    place = models.ForeignKey(
        'places.Place',
        on_delete=models.CASCADE,
        related_name='images',
    )

    class Meta:
        verbose_name = _('Place image')
        verbose_name_plural = _('Place images')

    def __str__(self) -> str:
        return f'{self.title} {self.order}'

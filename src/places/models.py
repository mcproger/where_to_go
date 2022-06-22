from app.models import Model, models
from django.utils.translation import gettext_lazy as _


class Place(Model):
    title = models.CharField(_('Title'), max_length=32, db_index=True)
    description_short = models.CharField(_('Short description of the place'), max_length=250, blank=True, null=True)
    description_long = models.TextField(_('Detailed description of the place'), blank=True, null=True)

    class Meta:
        verbose_name = _('Place')
        verbose_name_plural = _('Places')

    def __str__(self) -> str:
        return self.title

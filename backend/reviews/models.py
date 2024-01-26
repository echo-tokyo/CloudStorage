from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Review(models.Model):
    user = models.OneToOneField(
        verbose_name=_('user id'),
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    review_text = models.TextField(
        verbose_name=_('review text'),
        null=False,
        blank=False,
    )

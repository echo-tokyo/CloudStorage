from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Folder(models.Model):
    user = models.OneToOneField(
        verbose_name=_('user id'),
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        db_index=True,
    )
    name = models.CharField(
        verbose_name=_('folder name'),
        max_length=50,
        null=False,
        blank=False,
    )
    parent_id = models.ForeignKey(
        verbose_name=_('parent folder id'),
        to='self',
        on_delete=models.CASCADE,
        null=True,
    )
    recycle_bin = models.BooleanField(
        verbose_name=_('folder in recycle bin'),
        default=False,
    )
    star = models.BooleanField(
        verbose_name=_('starred'),
        default=False,
    )
    created_at = models.DateTimeField(
        verbose_name=_('created at'),
        auto_now_add=True,
        null=False,
        blank=False,
    )
    updated_at = models.DateTimeField(
        verbose_name=_('updated at'),
        auto_now=True,
        null=False,
        blank=False,
    )


class File(models.Model):
    name = models.CharField(
        verbose_name=_('file name'),
        max_length=50,
        null=False,
        blank=False,
    )
    size = models.CharField(
        verbose_name=_('file size'),
        max_length=20,
        null=False,
        blank=False,
    )
    path = models.FileField(
        verbose_name=_('path to file'),
        upload_to='files/',
        null=False,
        blank=False,
    )
    folder = models.ForeignKey(
        verbose_name=_('parent folder id'),
        to='self',
        on_delete=models.CASCADE,
        null=True,
    )
    recycle_bin = models.BooleanField(
        verbose_name=_('file in recycle bin'),
        default=False,
    )
    star = models.BooleanField(
        verbose_name=_('starred'),
        default=False,
    )
    created_at = models.DateTimeField(
        verbose_name=_('created at'),
        auto_now_add=True,
        null=False,
        blank=False,
    )

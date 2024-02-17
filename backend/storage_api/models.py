from datetime import datetime
from os import remove as remove_file

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


def user_files_dir_path(instance, filename):
    """return path to upload file to MEDIA_ROOT/files/user_<id>/<folder-id>_<datetime>"""

    # папка, в которой находится файл
    folder = instance.folder

    # получаем датавремя
    now_time = datetime.now()
    str_now_time = now_time.strftime('%Y_%m_%d_%H_%M_%S')

    if '.' in filename:
        splitted_filename = filename.split(".")
        # достаём расширение файла
        file_extension = splitted_filename[-1]
        # меняем имя файла, заданное юзером, на имя с id папки и точной датой до секунд
        return f'files/user_{folder.user.id}/{folder.pk}_{str_now_time}.{file_extension}'

    return f'files/user_{instance.folder.user.id}/{instance.folder.pk}_{str_now_time}_{filename[:10]}'


class Folder(models.Model):
    user = models.ForeignKey(
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
    parent = models.ForeignKey(
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
        auto_now_add=True,
        null=False,
        blank=False,
    )


class File(models.Model):
    user = models.ForeignKey(
        verbose_name=_('user id'),
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    name = models.CharField(
        verbose_name=_('file name'),
        max_length=50,
        null=False,
        blank=False,
    )
    size = models.IntegerField(
        verbose_name=_('file size'),
    )
    path = models.FileField(
        verbose_name=_('path to file'),
        upload_to=user_files_dir_path,
        null=False,
        blank=False,
    )
    folder = models.ForeignKey(
        verbose_name=_('parent folder id'),
        to=Folder,
        on_delete=models.CASCADE,
        null=False,
        blank=False
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

    @property
    def create_datetime_str(self):
        return str(self.created_at)[:16].replace('T', ' ')

    def delete(self, *args, **kwargs):
        full_file_path = f'{settings.BASE_DIR}/media/{self.path}'

        try:
            remove_file(full_file_path)
        except FileNotFoundError:
            pass

        # Вызов оригинального метода delete()
        super(File, self).delete(*args, **kwargs)

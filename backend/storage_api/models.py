from datetime import datetime
from os.path import exists as file_exist
from os import remove as remove_file

from django.conf import settings
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from .errors import FolderValueError


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

    @property
    def str_created_at(self):
        return str(self.created_at)[:16].replace('T', ' ')

    @property
    def str_updated_at(self):
        return str(self.created_at)[:16].replace('T', ' ')

    def delete(self, *args, **kwargs):
        # ошибка, если запрос на удаление корневой папки
        if self.name == '/':
            raise FolderValueError('Cannot delete root folder!')

        # Вызов оригинального метода delete()
        super(Folder, self).delete(*args, **kwargs)


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


# Функция для удаления связанных файлов перед удалением папки
@receiver(pre_delete, sender=Folder)
def delete_related_files(sender, instance, **kwargs):
    related_files = File.objects.filter(folder=instance)

    for file in related_files:
        # получение пути файла
        full_file_path = f'{settings.BASE_DIR}/media/{file.path}'

        # Удаление физического файла
        if file_exist(full_file_path):
            remove_file(full_file_path)

        # Удаление записи о файле из базы данных
        file.delete()


# Функция для удаления физического файла перед удалением его записи из БД
@receiver(pre_delete, sender=File)
def delete_related_files(sender, instance, **kwargs):
    full_file_path = f'{settings.BASE_DIR}/media/{instance.path}'

    try:
        remove_file(full_file_path)
    except FileNotFoundError:
        print('ERROR')
        pass

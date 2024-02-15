from django.utils.translation import gettext_lazy as _

from rest_framework import status
from rest_framework.exceptions import APIException


class FolderValueError(APIException):
    """Ошибка номера папки файла: неверные данные"""

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Value error')
    default_code = 'folder_value_error'


class FileNotGivenError(APIException):
    """Ошибка при нахождении файла: неверные данные о файле в теле запроса"""

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Param error')
    default_code = 'file_not_given_error'


class GetFileError(APIException):
    """Ошибка при нахождении файла: неверные данные о файле в теле запроса"""

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('File error')
    default_code = 'get_file_error'



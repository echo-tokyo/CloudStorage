from django.utils.translation import gettext_lazy as _

from rest_framework import status
from rest_framework.exceptions import APIException


class UserValidateError(APIException):
    """Ошибка в получении доступа: неверные данные о пользователе, неверный токен"""

    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _('Validate error')
    default_code = 'user_validate_error'


class UserAccessForbidden(APIException):
    """Ошибка в получении прав на доступ: юзер не авторизован, деактивирован"""

    status_code = status.HTTP_403_FORBIDDEN
    default_detail = _('Access forbidden')
    default_code = 'user_access_forbidden'


class ServerProcessError(APIException):
    """Ошибка в обработке токена"""

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = _('Process error')
    default_code = 'server_process_error'

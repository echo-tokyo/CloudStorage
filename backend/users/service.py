from .errors import ServerProcessError
from .models import Token, User


def delete_one_token(token: str):
    """Delete given token from table Token"""

    table_token = Token.objects.filter(token=token)

    if not table_token:
        raise ServerProcessError('Cannot process the token')

    try:
        table_token.delete()
    except Exception:
        raise ServerProcessError('Cannot delete the token')


def delete_tokens_when_change_passwd(cur_token: str, user: User):
    """Delete given token from table Token"""

    # получение всех токенов, кроме текущего
    user_tokens = Token.objects.filter(user=user.pk).exclude(token=cur_token)

    if not user_tokens:
        return

    try:
        # удаление полученных токенов
        for user_token in user_tokens:
            user_token.delete()
    except Exception:
        raise ServerProcessError("Cannot delete user's tokens")

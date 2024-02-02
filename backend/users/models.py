from datetime import datetime

import jwt

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from storage_api.models import Folder
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_('email'),
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        db_index=True,
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
    is_staff = models.BooleanField(
        verbose_name=_("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        verbose_name=_("active"),
        default=True,
        help_text=_("Should user be treated as active? Unselect this instead of deleting accounts."),
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    @property
    def token(self):
        """Get token"""
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        """Generate JWT-token with user id, expire in JWT_EXPIRE time"""

        token_create_time = datetime.now()
        token_expire_time = token_create_time + settings.JWT_EXPIRE
        user_id = self.pk
        token = jwt.encode({
            'id': user_id,
            'exp': int(token_expire_time.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        new_token_obj = Token.objects.create(
            user_id=user_id,
            token=token,
        )

        try:
            new_token_obj.save()
            return token
        except Exception as error:
            raise error

    def create_root_dir(self):
        """Create root dir for user"""

        new_folder = Folder.objects.create(user=self, name='/')
        return new_folder


class Token(models.Model):
    user = models.ForeignKey(
        verbose_name=_('user id'),
        to=User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        db_index=True,
    )
    token = models.CharField(
        verbose_name=_('token'),
        max_length=255,
        null=False,
        blank=False,
    )

    # blacklisted = models.BooleanField(
    #     verbose_name=_('blacklisted'),
    #     default=False
    # )

    class Meta:
        verbose_name = _('token')
        verbose_name_plural = _('tokens')

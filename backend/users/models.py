import jwt

from datetime import datetime
from random import randint

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

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
    nickname = models.CharField(
        verbose_name=_('nickname'),
        max_length=30,
        null=True,
        blank=True,
    )
    photo = models.ImageField(
        verbose_name=_('profile photo'),
        max_length=255,
        null=True,
        blank=True,
        default=settings.DEFAULT_PROFILE_PHOTO,
        upload_to='profile_photos/',
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

        dt = datetime.now() + settings.JWT_EXPIRE

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token

    def save(self, *args, **kwargs):
        # устанавливаем дефолтный ник, если он не задан
        if not self.nickname:
            rand_num = randint(1, 999999)
            self.nickname = _(f'User_{str(rand_num).rjust(6, "0")}')

        # устанавливаем дефолтное фото, если оно было очищено
        if not self.photo:
            self.photo = settings.DEFAULT_PROFILE_PHOTO

        super(User, self).save(*args, **kwargs)

from datetime import datetime

import jwt

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.dispatch import receiver
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
        try:
            new_folder = Folder.objects.create(user=self, name='/')
            return new_folder
        except Exception as error:
            raise error

    @property
    def root_dir(self):
        """Get root dir for user"""
        try:
            user_folder = Folder.objects.get(user=self, name='/')
            return user_folder
        except Exception as error:
            raise error


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


class Profile(models.Model):
    user = models.OneToOneField(
        verbose_name=_('user id'),
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        unique=True,
        primary_key=True,
    )
    photo = models.ImageField(
        verbose_name=_('profile photo'),
        max_length=255,
        null=True,
        blank=True,
        default=settings.DEFAULT_PROFILE_PHOTO,
        upload_to='profile_photos/',
    )

    # nickname = models.CharField(
    #     verbose_name=_('nickname'),
    #     max_length=30,
    #     null=True,
    #     blank=True,
    # )

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return f'http://{settings.IP_OR_DNS_SERVER}/static/{self.photo}'

    def save(self, *args, **kwargs):
        # # устанавливаем дефолтный ник, если он не задан
        # if not self.nickname:
        #     user_id = get_user_model().objects.get(email=self.user).id
        #     self.nickname = _(f'User_{str(user_id).rjust(6, "0")}')

        # устанавливаем дефолтное фото, если оно было очищено
        if not self.photo:
            self.photo = settings.DEFAULT_PROFILE_PHOTO

        super(Profile, self).save(*args, **kwargs)


@receiver(models.signals.post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create profile for user when user has been created"""
    if created:
        Profile.objects.create(user=instance)


@receiver(models.signals.post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Save profile for user when user has been created"""
    instance.profile.save()

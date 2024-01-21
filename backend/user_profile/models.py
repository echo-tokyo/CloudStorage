from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


DEFAULT_PROFILE_PHOTO = 'profile_photos/default_user_profile_photo.png'


class Profile(models.Model):
    user = models.OneToOneField(
        verbose_name=_('user id'),
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        unique=True,
        primary_key=True,
    )
    nickname = models.CharField(
        verbose_name=_('nickname'),
        max_length=50,
        null=True,
        blank=True,
    )
    photo = models.ImageField(
        verbose_name=_('profile photo'),
        max_length=255,
        null=True,
        blank=True,
        default=DEFAULT_PROFILE_PHOTO,
        upload_to='profile_photos/',
    )

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def save(self, *args, **kwargs):
        # устанавливаем дефолтный ник, если он не задан
        if not self.nickname:
            user_id = get_user_model().objects.get(email=self.user).id
            self.nickname = _(f'User_{str(user_id).rjust(6, "0")}')

        # устанавливаем дефолтное фото, если оно было очищено
        if not self.photo:
            self.photo = DEFAULT_PROFILE_PHOTO

        super(Profile, self).save(*args, **kwargs)


@receiver(models.signals.post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(models.signals.post_save, sender=get_user_model())
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

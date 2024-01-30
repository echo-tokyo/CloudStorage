from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


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


@receiver(models.signals.post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    """Create profile for user when user has been created"""
    if created:
        Profile.objects.create(user=instance)


@receiver(models.signals.post_save, sender=get_user_model())
def save_user_profile(sender, instance, **kwargs):
    """Save profile for user when user has been created"""
    instance.profile.save()

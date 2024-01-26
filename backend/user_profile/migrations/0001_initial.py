# Generated by Django 4.1 on 2024-01-25 07:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='user id')),
                ('nickname', models.CharField(blank=True, max_length=50, null=True, verbose_name='nickname')),
                ('photo', models.ImageField(blank=True, default='profile_photos/default_user_profile_photo.png', max_length=255, null=True, upload_to='profile_photos/', verbose_name='profile photo')),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
            },
        ),
    ]

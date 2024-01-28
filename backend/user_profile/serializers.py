from django.conf import settings
from rest_framework import serializers

from .models import Profile


class UserProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Profile
        fields = ('id', 'nickname', 'photo')

    def to_representation(self, instance):
        print(instance.photo)

        representation = {
            "id": instance.user.id,
            "nickname": instance.nickname,
            "photo": f'http://{settings.IP_OR_DNS_SERVER}/static/{instance.photo}'
        }
        return representation

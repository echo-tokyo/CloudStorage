from rest_framework import serializers

from .models import Profile


class GetUserProfileSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ('photo_url',)

    def get_photo_url(self, instance: Profile):
        return instance.photo_url

from rest_framework import serializers

from .models import Profile


class GetUserProfileSerializer(serializers.ModelSerializer):
    """serialization of getting user profile"""

    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ('photo_url',)

    def get_photo_url(self, instance: Profile):
        """Get full url to profile photo"""

        return instance.photo_url

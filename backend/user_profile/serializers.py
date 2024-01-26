from rest_framework import serializers

from .models import Profile


class UserProfileSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ('id', 'nickname', 'photo')

    def get_id(self, obj: Profile):
        """Return user_id as id"""
        return obj.user_id

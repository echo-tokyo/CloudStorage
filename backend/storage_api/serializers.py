from rest_framework import serializers

from .models import File, Folder


class UploadFileToServerSerializer(serializers.ModelSerializer):
    """Serialization of uploading file"""
    id = serializers.IntegerField(read_only=True)
    folder_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = File
        fields = ('id', 'name', 'size', 'path', 'folder_id', 'star', 'created_at')
        read_only_fields = ('star', 'created_at')
        extra_kwargs = {
            'path': {'write_only': True},
        }

    def create(self, validated_data):
        folder_id = validated_data.pop('folder_id')
        folder = Folder.objects.get(pk=folder_id)

        new_file = File.objects.create(folder=folder, **validated_data)
        return new_file

    def to_representation(self, instance: File):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.datetime_str
        return representation

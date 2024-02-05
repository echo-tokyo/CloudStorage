from rest_framework import serializers

from .models import File, Folder


class UploadFileToServerSerializer(serializers.ModelSerializer):
    """Serialization of uploading file"""

    id = serializers.IntegerField(read_only=True)
    folder_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = File
        exclude = ('folder', 'recycle_bin')
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
        representation['created_at'] = instance.create_datetime_str
        return representation


class GetFileListSerializer(serializers.ModelSerializer):
    """Serialization of file list of definite folder"""

    folder_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = File
        exclude = ('folder', 'recycle_bin', 'path')

    def to_representation(self, instance: File):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.create_datetime_str
        return representation


# class DownloadFileFromServerSerializer(serializers.ModelSerializer):
#     path = serializers.FileField(write_only=True)
#
#     class Meta:
#         model = File
#         fields = ('id', 'path')
#         read_only_fields = ('id',)
#
#     def validate(self, data):
#         file_id = data.get('id', None)
#
#         print(file_id)
#
#         return data
#
#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#
#         print(representation)
#         return representation

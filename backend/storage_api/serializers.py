from rest_framework import serializers

from users.errors import UserValidateError, UserAccessForbidden
from .errors import GetFileError, FolderValueError
from .models import File, Folder


class UploadFileToServerSerializer(serializers.ModelSerializer):
    """Serialization of uploading file"""

    id = serializers.IntegerField(read_only=True)
    folder_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = File
        exclude = ('user', 'folder', 'recycle_bin')
        read_only_fields = ('star', 'created_at')
        extra_kwargs = {
            'path': {'write_only': True},
        }

    def create(self, validated_data):
        # получение юзера из контекста
        user = self.context.get('user', None)
        if user is None:
            raise UserValidateError('Cannot parse user from request.')

        folder_id = validated_data.pop('folder_id')
        folder = Folder.objects.get(pk=folder_id)

        new_file = File.objects.create(folder=folder, user=user, **validated_data)
        return new_file

    def to_representation(self, instance: File):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.create_datetime_str
        return representation


class DownloadFileFromServerSerializer(serializers.ModelSerializer):
    """Serialization of downloading file"""
    id = serializers.IntegerField(write_only=True)

    class Meta:
        model = File
        fields = ('id', 'path', 'name')
        read_only_fields = ('path', 'name')

    def validate(self, data):
        # получение юзера из контекста
        user = self.context.get('user', None)
        if user is None:
            raise UserValidateError('Cannot parse user from request.')

        try:
            # достаём id файла из JSON-запроса
            file_id = data.get('id', None)
            # получение объекта файла
            file_obj = File.objects.get(id=file_id)
        except File.DoesNotExist:
            raise GetFileError('Cannot get file. Invalid file id was given.')

        try:
            # получение объекта папки
            folder = Folder.objects.get(id=file_obj.folder.id)
        except Exception:
            raise FolderValueError('Folder with given file not found')

        if folder.user != user:
            raise UserAccessForbidden('User have no permissions to get requested file!')

        validated_data = {
            "name": file_obj.name,
            "path": file_obj.path,
        }

        return validated_data


class GetFileListSerializer(serializers.ModelSerializer):
    """Serialization of file list of definite folder"""

    class Meta:
        model = File
        exclude = ('folder', 'recycle_bin', 'path', 'user')

    def to_representation(self, instance: File):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.create_datetime_str
        return representation


class GetFolderListSerializer(serializers.ModelSerializer):
    """Serialization of folder list of definite folder"""

    class Meta:
        model = Folder
        exclude = ('parent', 'recycle_bin', 'user')

    def to_representation(self, instance: Folder):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.str_created_at
        representation['updated_at'] = instance.str_updated_at
        return representation


class MoveFileToTrashSerializer(serializers.ModelSerializer):
    """Serialization of moving file to recycle bin"""

    class Meta:
        model = File
        fields = ('id',)

    def update(self, instance: File, validated_data):
        # перемещение файла в корзину
        instance.recycle_bin = 1
        instance.save()

        return instance


class MoveFileFromTrashSerializer(serializers.ModelSerializer):
    """Serialization of moving file from recycle bin"""

    class Meta:
        model = File
        fields = ('id',)

    def update(self, instance: File, validated_data):
        # перемещение файла из корзины
        instance.recycle_bin = 0
        instance.save()

        return instance


class MoveFolderToTrashSerializer(serializers.ModelSerializer):
    """Serialization of moving folder to recycle bin"""

    class Meta:
        model = Folder
        fields = ('id',)

    def update(self, instance: Folder, validated_data):
        # перемещение папки в корзину
        instance.recycle_bin = 1
        instance.save()

        return instance


class MoveFolderFromTrashSerializer(serializers.ModelSerializer):
    """Serialization of moving folder to recycle bin"""

    class Meta:
        model = Folder
        fields = ('id',)

    def update(self, instance: Folder, validated_data):
        # перемещение папки из корзины
        instance.recycle_bin = 0
        instance.save()

        return instance


class CreateFolderSerializer(serializers.ModelSerializer):
    """Serialization of creating new folder"""

    class Meta:
        model = Folder
        exclude = ('user', 'recycle_bin')
        read_only_fields = ('star', 'created_at', 'updated_at')
        extra_kwargs = {
            'parent': {'write_only': True},
        }

    def create(self, validated_data):
        # получение юзера из контекста
        user = self.context.get('user', None)
        if user is None:
            raise UserValidateError('Cannot parse user from request.')

        new_file = Folder.objects.create(user=user, **validated_data)
        return new_file

    def to_representation(self, instance: Folder):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.str_created_at
        representation['updated_at'] = instance.str_updated_at
        return representation


class RenameFolderSerializer(serializers.ModelSerializer):
    """Serialization of creating new folder"""

    class Meta:
        model = Folder
        exclude = ('user', 'recycle_bin', 'parent')
        read_only_fields = ('star', 'created_at', 'updated_at')

    def update(self, instance: Folder, validated_data):
        instance.name = validated_data.get('name')
        instance.save()

        return instance

    def to_representation(self, instance: Folder):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.str_created_at
        representation['updated_at'] = instance.str_updated_at
        return representation

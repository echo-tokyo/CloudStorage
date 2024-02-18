from django.conf import settings
from django.http import FileResponse

from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from users.errors import UserValidateError, UserAccessForbidden
from .errors import FolderValueError, FileNotGivenError, GetFileError, GetFolderError
from .serializers import (UploadFileToServerSerializer, DownloadFileFromServerSerializer,
                          GetFileListSerializer, GetFolderListSerializer,
                          MoveFileToTrashSerializer, MoveFileFromTrashSerializer,
                          CreateFolderSerializer, RenameFolderSerializer,
                          MoveFolderToTrashSerializer, MoveFolderFromTrashSerializer)
from .models import Folder, File


class GetRootDirAPIView(APIView):
    """Get root dir for current user"""

    def get(self, request: Request):
        user = request.user

        data = {
            'root_dir': user.root_dir.id
        }

        return Response(data=data, status=status.HTTP_200_OK)


class UploadFileToServerAPIView(APIView):
    """Client save file on server"""

    parser_classes = (MultiPartParser,)
    permission_classes = (IsAuthenticated,)
    serializer_class = UploadFileToServerSerializer

    def post(self, request: Request):
        data = request.data

        try:
            folder_id = int(data.get('folder_id'))
            folder = Folder.objects.get(pk=folder_id)
            # проверка на принадлежность папки юзеру
            if folder.user != request.user:
                raise ValueError

        except (ValueError, TypeError):
            raise FolderValueError('Invalid folder id was given')

        try:
            file = data.get('file')
        except Exception:
            raise FileNotGivenError('File to upload not given')

        file_data = {
            "path": file,
            "name": file.name,
            "size": file.size,
            "folder_id": folder_id
        }

        # Добавление пользователя из запроса в контекст
        self.serializer_class.context = {'user': request.user}

        serializer = self.serializer_class(data=file_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class DownloadFileFromServerAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DownloadFileFromServerSerializer

    def post(self, request: Request):
        # Добавление пользователя из запроса в контекст
        self.serializer_class.context = {'user': request.user}

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # достаём из словаря path и name запрашиваемого файла
        file_path = str(settings.BASE_DIR) + serializer.data.get('path')
        file_name = serializer.data.get('name')

        # отправляем файл
        return FileResponse(
            open(file_path, 'rb'),
            as_attachment=True,
            filename=file_name,
            status=status.HTTP_200_OK,
        )


class GetFolderContentAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_files(self, request: Request, folder_id: int) -> GetFileListSerializer:
        files_queryset = File.objects.filter(folder_id=folder_id, recycle_bin=0)
        file_serializer = GetFileListSerializer(files_queryset, many=True)

        return file_serializer

    def get_folders(self, request: Request, folder_id: int) -> GetFolderListSerializer:
        folders_queryset = Folder.objects.filter(parent=folder_id, recycle_bin=0)
        folder_serializer = GetFolderListSerializer(folders_queryset, many=True)

        return folder_serializer

    def post(self, request: Request):
        try:
            folder_id = int(request.data.get('folder_id'))
            folder = Folder.objects.get(pk=folder_id)
            # проверка на принадлежность папки юзеру
            if folder.user != request.user:
                raise ValueError

        except (ValueError, TypeError):
            raise FolderValueError('Invalid folder id was given')
        except Folder.DoesNotExist:
            raise FolderValueError('Cannot get folder. Invalid folder id was given')

        # получение сериализатора файлов
        file_serializer = self.get_files(request=request, folder_id=folder_id)
        # получение сериализатора вложенных папок
        folder_serializer = self.get_folders(request=request, folder_id=folder_id)
        # получение id родительской папки
        try:
            parent_id = folder.parent.id
        except AttributeError:
            # если нет родительской папки (запрашиваемая папка - корневая)
            parent_id = None

        content_data = {
            'parent': parent_id,
            'files': file_serializer.data,
            'folders': folder_serializer.data,
        }

        return Response(data=content_data, status=status.HTTP_200_OK)


class GetTrashAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_files(self, request: Request) -> GetFileListSerializer:
        files_queryset = File.objects.filter(user=request.user, recycle_bin=1)
        file_serializer = GetFileListSerializer(files_queryset, many=True)

        return file_serializer

    def get_folders(self, request: Request) -> GetFolderListSerializer:
        folders_queryset = Folder.objects.filter(user=request.user, recycle_bin=1)
        folder_serializer = GetFolderListSerializer(folders_queryset, many=True)

        return folder_serializer

    def post(self, request: Request):
        # получение сериализатора файлов
        file_serializer = self.get_files(request=request)
        # получение сериализатора вложенных папок
        folder_serializer = self.get_folders(request=request)

        content_data = {
            'files': file_serializer.data,
            'folders': folder_serializer.data,
        }

        return Response(data=content_data, status=status.HTTP_200_OK)


class MoveFileToTrashAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MoveFileToTrashSerializer

    def put(self, request: Request):
        # получение юзера из запроса
        user = request.user
        if user is None:
            raise UserValidateError('Cannot parse user from request.')

        try:
            # достаём id файла из запроса
            file_id = request.data.get('id', None)
            # получение объекта файла
            file_obj = File.objects.get(id=file_id)
        except File.DoesNotExist:
            raise GetFileError('Cannot get file. Invalid file id was given.')

        if file_obj.user != user:
            raise UserAccessForbidden('User have no permissions to move this file to recycle bin!')

        serializer = self.serializer_class(data=request.data, instance=file_obj)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class MoveFileFromTrashAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MoveFileFromTrashSerializer

    def put(self, request: Request):
        # получение юзера из запроса
        user = request.user
        if user is None:
            raise UserValidateError('Cannot parse user from request.')

        try:
            # достаём id файла из запроса
            file_id = request.data.get('id', None)
            # получение объекта файла
            file_obj = File.objects.get(id=file_id)
        except File.DoesNotExist:
            raise GetFileError('Cannot get file. Invalid file id was given.')

        if file_obj.user != user:
            raise UserAccessForbidden('User have no permissions to move this file from recycle bin!')

        serializer = self.serializer_class(data=request.data, instance=file_obj)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class MoveFolderToTrashAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MoveFolderToTrashSerializer

    def put(self, request: Request):
        # получение юзера из запроса
        user = request.user
        if user is None:
            raise UserValidateError('Cannot parse user from request.')

        try:
            # достаём id папки из запроса
            folder_id = request.data.get('id', None)
            # получение объекта папки
            folder_obj = Folder.objects.get(id=folder_id)
        except Folder.DoesNotExist:
            raise GetFolderError('Cannot get folder. Invalid folder id was given.')

        if folder_obj.user != user:
            raise UserAccessForbidden('User have no permissions to move this folder to recycle bin!')

        if folder_obj.name == '/':
            raise FolderValueError('Cannot move root folder to trash!')

        serializer = self.serializer_class(data=request.data, instance=folder_obj)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class MoveFolderFromTrashAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MoveFolderFromTrashSerializer

    def put(self, request: Request):
        # получение юзера из запроса
        user = request.user
        if user is None:
            raise UserValidateError('Cannot parse user from request.')

        try:
            # достаём id папки из запроса
            folder_id = request.data.get('id', None)
            # получение объекта папки
            folder_obj = Folder.objects.get(id=folder_id)
        except Folder.DoesNotExist:
            raise GetFolderError('Cannot get folder. Invalid folder id was given.')

        if folder_obj.user != user:
            raise UserAccessForbidden('User have no permissions to move this folder from recycle bin!')

        if folder_obj.name == '/':
            raise FolderValueError('Cannot move root folder from trash!')

        serializer = self.serializer_class(data=request.data, instance=folder_obj)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class DeleteFileAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request: Request):
        # получение юзера из запроса
        user = request.user
        if user is None:
            raise UserValidateError('Cannot parse user from request.')

        try:
            # достаём id файла из запроса
            file_id = request.data.get('id', None)
            # получение объекта файла
            file_obj = File.objects.get(id=file_id)
        except File.DoesNotExist:
            raise GetFileError('Cannot get file. Invalid file id was given.')

        if file_obj.user != user:
            raise UserAccessForbidden('User have no permissions to move this file to recycle bin!')

        try:
            # удаление файла
            file_obj.delete()
        except Exception as error:
            raise error

        return Response(status=status.HTTP_200_OK)


class CreateFolderAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CreateFolderSerializer

    def post(self, request: Request):
        data = request.data

        # Добавление пользователя из запроса в контекст
        self.serializer_class.context = {'user': request.user}

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class DeleteFolderAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request: Request):
        # получение юзера из запроса
        user = request.user
        if user is None:
            raise UserValidateError('Cannot parse user from request.')

        try:
            # достаём id папки из запроса
            folder_id = request.data.get('id', None)
            # получение объекта файла
            folder_obj = Folder.objects.get(id=folder_id)
        except Folder.DoesNotExist:
            raise GetFileError('Cannot get folder. Invalid folder id was given.')

        if folder_obj.user != user:
            raise UserAccessForbidden('User have no permissions to move this file to recycle bin!')

        if folder_obj.name == '/':
            raise FolderValueError('Cannot remove root folder!')

        try:
            # удаление файла
            folder_obj.delete()
        except Exception as error:
            raise error

        return Response(status=status.HTTP_200_OK)


class RenameFolderAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RenameFolderSerializer

    def put(self, request: Request):
        data = request.data

        try:
            folder_id = data.get('id')
            folder_obj = Folder.objects.get(id=folder_id)
        except Folder.DoesNotExist:
            raise FolderValueError('Cannot get folder. Invalid folder id was given.')

        serializer = self.serializer_class(data=data, instance=folder_obj)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_200_OK)


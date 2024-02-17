from django.conf import settings
from django.http import FileResponse

from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .errors import FolderValueError, FileNotGivenError
from .serializers import (UploadFileToServerSerializer, DownloadFileFromServerSerializer, GetFileListSerializer,
                          GetTrashSerializer)
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


class GetFileListAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = GetFileListSerializer

    def post(self, request: Request):
        try:
            folder_id = int(request.data.get('folder_id'))
            folder = Folder.objects.get(pk=folder_id)
            # проверка на принадлежность папки юзеру
            if folder.user != request.user:
                raise ValueError

        except (ValueError, TypeError):
            raise FolderValueError('Invalid folder id was given')

        files_queryset = File.objects.filter(folder_id=folder_id, recycle_bin=0)
        serializer = self.serializer_class(files_queryset, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class GetTrashAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = GetTrashSerializer

    def post(self, request: Request):
        user = request.user

        files_queryset = File.objects.filter(recycle_bin=1, user=user)
        serializer = self.serializer_class(files_queryset, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class MoveToTrashAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    # serializer_class = MoveToTrashSerializer

    def post(self, request: Request):
        ...

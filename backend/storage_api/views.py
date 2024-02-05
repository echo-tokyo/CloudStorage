from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .errors import FolderValueError, FileNotGivenError
from .serializers import UploadFileToServerSerializer, GetFileListSerializer
from .models import Folder, File


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

        serializer = self.serializer_class(data=file_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class GetFileListAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = GetFileListSerializer

    def get(self, request: Request):
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


# class DownloadFileFromServerAPIView(APIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = DownloadFileFromServerSerializer
#
#     def post(self, request: Request):
#         # from django.http import FileResponse
#         # response = FileResponse(open('myfile.png', 'rb'))
#
#         data = request.data
#
#         print('request.user', request.user)
#         print('data', data)
#
#         serializer = self.serializer_class(data=data)
#         serializer.is_valid(raise_exception=True)
#
#         print('serializer.data', serializer.data)
#
#         # return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_201_CREATED)

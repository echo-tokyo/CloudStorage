from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .errors import FolderValueError, FileNotGivenError
from .serializers import UploadFileToServerSerializer
from .models import Folder


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

            if folder.user != request.user:
                print('ERROR')
                raise ValueError

        except (ValueError, TypeError):
            raise FolderValueError('Invalid folder id was given')

        try:
            file = data.get('file')
            # print(dir(file))
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

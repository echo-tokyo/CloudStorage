from django.urls import path

from .views import (GetRootDirAPIView, GetFileListAPIView,
                    UploadFileToServerAPIView, DownloadFileFromServerAPIView)


urlpatterns = [
    path('get-root-dir/', GetRootDirAPIView.as_view()),
    path('get-file-list/', GetFileListAPIView.as_view()),

    path('upload-file-to-server/', UploadFileToServerAPIView.as_view()),
    path('download-file-from-server/', DownloadFileFromServerAPIView.as_view()),
]

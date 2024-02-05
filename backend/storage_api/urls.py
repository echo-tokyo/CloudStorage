from django.urls import path

from .views import (GetRootDirAPIView,
                    UploadFileToServerAPIView, GetFileListAPIView)


urlpatterns = [
    path('get-root-dir/', GetRootDirAPIView.as_view()),
    path('get-file-list/', GetFileListAPIView.as_view()),

    path('upload-file-to-server/', UploadFileToServerAPIView.as_view()),
    # path('download-file-from-server/', DownloadFileFromServerAPIView.as_view()),
]

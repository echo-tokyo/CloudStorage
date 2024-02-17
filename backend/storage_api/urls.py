from django.urls import path

from .views import (GetRootDirAPIView, GetFileListAPIView,
                    UploadFileToServerAPIView, DownloadFileFromServerAPIView,
                    GetTrashAPIView, MoveToTrashAPIView)


urlpatterns = [
    path('get-root-dir/', GetRootDirAPIView.as_view()),
    path('get-file-list/', GetFileListAPIView.as_view()),

    path('upload-file-to-server/', UploadFileToServerAPIView.as_view()),
    path('download-file-from-server/', DownloadFileFromServerAPIView.as_view()),

    path('get-trash/', GetTrashAPIView.as_view()),
    path('move-to-trash/', MoveToTrashAPIView.as_view()),
    # path('move-from-trash/', DownloadFileFromServerAPIView.as_view()),
    # path('delete-file/', DownloadFileFromServerAPIView.as_view()),
]

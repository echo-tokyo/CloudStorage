from django.urls import path

from .views import UploadFileToServerAPIView, GetFileListAPIView


urlpatterns = [
    path('get-file-list/', GetFileListAPIView.as_view()),
    path('upload-file-to-server/', UploadFileToServerAPIView.as_view()),
    # path('download-file-from-server/', DownloadFileFromServerAPIView.as_view()),
]

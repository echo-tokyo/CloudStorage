from django.urls import path

from .views import UploadFileToServerAPIView


urlpatterns = [
    # path('get-file-list/'),

    path('upload-file-to-server/', UploadFileToServerAPIView.as_view()),
    # path('download-file-from-server/'),
]

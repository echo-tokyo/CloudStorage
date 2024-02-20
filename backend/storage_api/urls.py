from django.urls import path

from .views import (GetRootDirAPIView, GetFolderContentAPIView,
                    UploadFileToServerAPIView, DownloadFileFromServerAPIView,
                    GetTrashAPIView, ClearTrashAPIView,
                    MoveFileToTrashAPIView, MoveFileFromTrashAPIView, DeleteFileAPIView,
                    CreateFolderAPIView, DeleteFolderAPIView, RenameFolderAPIView,
                    MoveFolderToTrashAPIView, MoveFolderFromTrashAPIView)


urlpatterns = [
    path('get-root-dir/', GetRootDirAPIView.as_view()),
    path('get-folder-content/', GetFolderContentAPIView.as_view()),

    path('upload-file-to-server/', UploadFileToServerAPIView.as_view()),
    path('download-file-from-server/', DownloadFileFromServerAPIView.as_view()),

    path('get-trash/', GetTrashAPIView.as_view()),
    path('clear-trash/', ClearTrashAPIView.as_view()),

    path('move-file-to-trash/', MoveFileToTrashAPIView.as_view()),
    path('move-file-from-trash/', MoveFileFromTrashAPIView.as_view()),
    path('delete-file/', DeleteFileAPIView.as_view()),

    path('move-folder-to-trash/', MoveFolderToTrashAPIView.as_view()),
    path('move-folder-from-trash/', MoveFolderFromTrashAPIView.as_view()),

    path('create-folder/', CreateFolderAPIView.as_view()),
    path('rename-folder/', RenameFolderAPIView.as_view()),
    path('delete-folder/', DeleteFolderAPIView.as_view()),
]

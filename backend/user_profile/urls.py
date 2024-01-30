from django.urls import path

from .views import GetUserProfileAPIView, EditUserProfileAPIView


urlpatterns = [
    path('get/', GetUserProfileAPIView.as_view()),
    path('edit-photo/', EditUserProfileAPIView.as_view()),
]

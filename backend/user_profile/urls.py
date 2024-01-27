from django.urls import path

from .views import UserProfileAPIView, EditUserProfileAPIView


urlpatterns = [
    path('get/', UserProfileAPIView.as_view()),

    path('edit/', EditUserProfileAPIView.as_view()),
]

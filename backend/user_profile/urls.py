from django.urls import path

from .views import UserProfileAPIView


urlpatterns = [
    path('get/', UserProfileAPIView.as_view()),
]

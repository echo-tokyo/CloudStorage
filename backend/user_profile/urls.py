from django.urls import path

from .views import UserProfileAPIView


urlpatterns = [
    path('', UserProfileAPIView.as_view()),
]

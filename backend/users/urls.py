from django.urls import path

from .views import UserRegistrationAPIView, UserLoginAPIView


urlpatterns = [
    path('reg/', UserRegistrationAPIView.as_view()),
    path('login/', UserLoginAPIView.as_view()),
]

from django.urls import path

from .views import UserRegistrationAPIView, UserLoginAPIView, GetTokenAPIView


urlpatterns = [
    path('reg/', UserRegistrationAPIView.as_view()),
    path('login/', UserLoginAPIView.as_view()),
    path('new-token/', GetTokenAPIView.as_view()),
]

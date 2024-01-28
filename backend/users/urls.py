from django.urls import path

from .views import (UserRegistrationAPIView, UserLoginAPIView,
                    EditUserAPIView, ChangeUserPasswordAPIView,
                    GetTokenAPIView)


urlpatterns = [
    path('reg/', UserRegistrationAPIView.as_view()),
    path('login/', UserLoginAPIView.as_view()),

    path('edit/', EditUserAPIView.as_view()),
    path('change-password/', ChangeUserPasswordAPIView.as_view()),

    path('new-token/', GetTokenAPIView.as_view()),
]

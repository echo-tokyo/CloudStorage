from django.urls import path

from .views import (UserRegistrationAPIView, UserLoginAPIView, UserLogoutAPIView,
                    EditUserAPIView, ChangeUserPasswordAPIView)


urlpatterns = [
    path('reg/', UserRegistrationAPIView.as_view()),
    path('login/', UserLoginAPIView.as_view()),
    path('logout/', UserLogoutAPIView.as_view()),

    path('edit/', EditUserAPIView.as_view()),
    path('change-password/', ChangeUserPasswordAPIView.as_view()),
]

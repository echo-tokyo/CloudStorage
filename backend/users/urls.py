from django.urls import path

from .views import (UserRegistrationAPIView, UserLoginAPIView, UserLogoutAPIView,
                    EditUserAPIView, ChangeUserPasswordAPIView,
                    GetUserProfileAPIView, EditUserProfileAPIView)


urlpatterns = [
    path('reg/', UserRegistrationAPIView.as_view()),
    path('login/', UserLoginAPIView.as_view()),
    path('logout/', UserLogoutAPIView.as_view()),

    path('edit-email/', EditUserAPIView.as_view()),
    path('change-password/', ChangeUserPasswordAPIView.as_view()),

    path('get-profile-info/', GetUserProfileAPIView.as_view()),
    path('edit-profile-photo/', EditUserProfileAPIView.as_view()),
]

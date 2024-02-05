from django.http import JsonResponse

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from .serializers import (UserRegistrationSerializer, UserLoginSerializer,
                          EditUserSerializer, ChangeUserPasswordSerializer,
                          GetUserProfileSerializer)
from .service import delete_tokens_when_change_passwd, delete_one_token
from .models import Profile


class UserRegistrationAPIView(APIView):
    """Registrate new user"""

    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

    def post(self, request: Request):
        # вытаскиваем данные из запроса
        user = request.data

        # обрабатываем данные в сериализаторе
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # возвращаем успех
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserLoginAPIView(APIView):
    """Login existing new user"""

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request: Request):
        user = request.data

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        # возвращаем успех
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserLogoutAPIView(APIView):
    """Logout for user"""

    permission_classes = (IsAuthenticated,)

    def post(self, request: Request):
        token = request.auth

        delete_one_token(token=token)

        # ответ об успехе
        response = JsonResponse(data={'result': 'Logout successfully!'}, status=status.HTTP_200_OK)
        return response


class EditUserAPIView(APIView):
    """Edit existing user email"""

    permission_classes = (IsAuthenticated,)
    serializer_class = EditUserSerializer

    def put(self, request: Request):
        # обрабатываем данные в сериализаторе
        serializer = self.serializer_class(instance=request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # возвращаем успех
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChangeUserPasswordAPIView(APIView):
    """Change user password"""

    permission_classes = (IsAuthenticated,)
    serializer_class = ChangeUserPasswordSerializer

    def put(self, request: Request):
        # вытаскиваем данные о юзере из запроса
        user = request.user
        token = request.auth

        # Добавление пользователя из запроса в контекст
        self.serializer_class.context = {'user': user}

        # обрабатываем данные в сериализаторе
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        delete_tokens_when_change_passwd(user=user, cur_token=token)

        # возвращаем успех
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetUserProfileAPIView(APIView):
    """Get user profile info (photo)"""

    permission_classes = (IsAuthenticated,)
    serializer_class = GetUserProfileSerializer

    def get(self, request: Request):
        # получение профиля юзера по его данным
        user_profile = Profile.objects.get(user_id=request.user.id)
        # обработка в сериализаторе
        serializer = self.serializer_class(instance=user_profile)

        # возвращаем данные
        return Response(serializer.data, status=status.HTTP_200_OK)


class EditUserProfileAPIView(APIView):
    """Edit user's profile info (photo)"""
    ...

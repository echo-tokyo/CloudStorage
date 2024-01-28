from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from .serializers import (UserRegistrationSerializer, UserLoginSerializer,
                          EditUserSerializer, ChangeUserPasswordSerializer,
                          GetTokenSerializer)


class UserRegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

    def post(self, request: Request):
        user = request.data

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserLoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request: Request):
        user = request.data

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        # print(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)


class EditUserAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = EditUserSerializer

    def patch(self, request: Request):
        # print('request.data', request.data)

        serializer = self.serializer_class(instance=request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # print('serializer.data', serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ChangeUserPasswordAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangeUserPasswordSerializer

    def put(self, request: Request):
        user = request.user

        # Добавление пользователя из запроса в контекст
        self.serializer_class.context = {'user': user}

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetTokenAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = GetTokenSerializer

    def post(self, request: Request):
        user = request.user

        user_data = {
            'id': user.id,
            'token': user.token,
        }
        print(user_data)

        serializer = self.serializer_class(data=user_data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Serialization of new user registration"""

    # не может быть прочитан клиентской стороной
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    # не может быть отправлен в запросе клиентской стороной
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'token')
        read_only_fields = ('id',)

    def create(self, validated_data):
        new_user = User.objects.create_user(**validated_data)
        return new_user


class UserLoginSerializer(serializers.Serializer):
    """Serialization of user login"""

    id = serializers.IntegerField(read_only=True)
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        """Checking the UserLoginSerializer for validity"""

        email = data.get('email', None)
        password = data.get('password', None)

        # Вызвать исключение, если не предоставлена почта.
        if email is None:
            raise serializers.ValidationError('An email address is required to log in.')
        # Вызвать исключение, если не предоставлен пароль.
        if password is None:
            raise serializers.ValidationError('A password is required to log in.')

        # проверка, что предоставленные почта и пароль соответствуют какому-то юзеру в БД
        user = authenticate(username=email, password=password)

        # если пользователь с данными почтой/паролем не найден
        if user is None:
            raise serializers.ValidationError('A user with this email and password was not found.')
        # если юзер деактивирован или заблокирован.
        if not user.is_active:
            raise serializers.ValidationError('This user has been deactivated.')

        # возвращаем словарь проверенных данных
        return {
            'id': user.id,
            'email': user.email,
            'token': user.token,
        }


class GetTokenSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    token = serializers.CharField(max_length=255)

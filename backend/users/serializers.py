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
        fields = ('email', 'password', 'token')

    def create(self, validated_data):
        new_user = User.objects.create_user(**validated_data)
        return new_user


class UserLoginSerializer(serializers.Serializer):
    """Serialization of user login"""

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
            'email': user.email,
            'token': user.token,
        }


class EditUserSerializer(serializers.Serializer):
    """Serializer for edit user's email or password or both"""

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password')

    def update(self, instance, validated_data):
        new_email = validated_data.get('email', instance.email)
        new_password = validated_data.get('password', None)

        instance.email = new_email
        if new_password is not None:
            instance.set_password(new_password)

        instance.save()
        return instance


class GetTokenSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    token = serializers.CharField(max_length=255)

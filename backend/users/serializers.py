from django.contrib.auth import authenticate
from django.db.utils import IntegrityError
from rest_framework import serializers

from .errors import UserValidateError, UserAccessForbidden
from .models import User, Profile


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Serialization of new user registration"""

    email = serializers.CharField(max_length=255, write_only=True)
    # не может быть прочитан клиентской стороной
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    # не может быть отправлен в запросе клиентской стороной
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'token')

    def create(self, validated_data):
        try:
            new_user = User.objects.create_user(**validated_data)
            new_user.create_root_dir()
        except IntegrityError:
            raise UserValidateError('Invalid email. User with such email already exist!')

        return new_user


class UserLoginSerializer(serializers.ModelSerializer):
    """Serialization of user login"""

    email = serializers.CharField(max_length=255, write_only=True)
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'token')

    def validate(self, data):
        """Checking the UserLoginSerializer for validity"""

        email = data.get('email', None)
        password = data.get('password', None)

        # Вызвать исключение, если не предоставлена почта.
        if email is None:
            raise UserValidateError('An email address is required to log in.')
        # Вызвать исключение, если не предоставлен пароль.
        if password is None:
            raise UserValidateError('A password is required to log in.')

        # проверка, что предоставленные почта и пароль соответствуют какому-то юзеру в БД
        user = authenticate(username=email, password=password)

        # если пользователь с данными почтой/паролем не найден
        if user is None:
            raise UserValidateError('A user with this email and password was not found.')
        # если юзер деактивирован или заблокирован.
        if not user.is_active:
            raise UserAccessForbidden('This user has been deactivated.')

        # возвращаем словарь проверенных данных
        return {
            'token': user.token,
        }


class EditUserSerializer(serializers.ModelSerializer):
    """Serializer for edit user's email"""

    class Meta:
        model = User
        fields = ('email',)

    def update(self, instance: User, validated_data):
        new_email = validated_data.get('email', instance.email)
        instance.email = new_email
        instance.save()
        return instance


class ChangeUserPasswordSerializer(serializers.Serializer):
    """Serializer for edit user's password"""

    old_password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    new_password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    result = serializers.CharField(read_only=True)

    def validate(self, data):
        old_password = data.get('old_password', None)
        new_password = data.get('new_password', None)

        # Вызвать исключение, если не предоставлен старый пароль.
        if old_password is None:
            raise UserValidateError('An old_password address is required to change password.')
        # Вызвать исключение, если не предоставлен новый пароль.
        if new_password is None:
            raise UserValidateError('A new_password is required to change password.')

        email = self.context.get('user', None).email
        if email is None:
            raise UserValidateError('Cannot parse email to change password.')

        # проверка, что предоставленные почта и пароль соответствуют какому-то юзеру в БД
        user = authenticate(username=email, password=old_password)

        # если пользователь с данными почтой/паролем не найден
        if user is None:
            raise UserValidateError('A user with this email and password was not found.')
        # если юзер деактивирован или заблокирован.
        if not user.is_active:
            raise UserAccessForbidden('This user has been deactivated.')

        # возвращаем словарь проверенных данных
        return {
            'new_password': new_password,
        }

    def create(self, validated_data):
        user = self.context.get('user', None)

        new_password = validated_data.get('new_password', None)
        if new_password is not None:
            user.set_password(new_password)

        user.save()
        return user

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['result'] = 'Password was changed successfully!'
        return representation


class GetUserProfileSerializer(serializers.ModelSerializer):
    """serialization of getting user profile"""

    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ('photo_url',)

    def get_photo_url(self, instance: Profile):
        """Get full url to profile photo"""

        return instance.photo_url

    def to_representation(self, instance: Profile):
        representation = super().to_representation(instance)
        # добавление email юзера к ответу
        representation['email'] = instance.user.email
        return representation

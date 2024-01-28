from re import sub as re_sub

from django.conf import settings
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
        fields = ('email', 'password', 'token', 'nickname', 'photo')
        read_only_fields = ('nickname', 'photo')

    def create(self, validated_data):
        new_user = User.objects.create_user(**validated_data)
        return new_user

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        photo_path_part = re_sub('^/media/', '', representation['photo'])
        representation['photo'] = f'http://{settings.IP_OR_DNS_SERVER}/static/{photo_path_part}'

        return representation


class UserLoginSerializer(serializers.ModelSerializer):
    """Serialization of user login"""

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'token', 'nickname', 'photo')
        read_only_fields = ('nickname', 'photo')

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
            'nickname': user.nickname,
            'photo': user.photo,
        }

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        photo_path_part = re_sub('^/media/', '', representation['photo'])
        representation['photo'] = f'http://{settings.IP_OR_DNS_SERVER}/static/{photo_path_part}'

        return representation


class EditUserSerializer(serializers.ModelSerializer):
    """Serializer for edit user's email or password or both"""

    class Meta:
        model = User
        fields = ('email', 'nickname')

    def update(self, instance: User, validated_data):
        new_email = validated_data.get('email', instance.email)
        new_nickname = validated_data.get('nickname', instance.nickname)
        # new_password = validated_data.get('password', None)
        # new_photo = validated_data.get('photo', instance.photo)

        instance.email = new_email
        instance.nickname = new_nickname
        # instance.photo = new_photo
        # if new_password is not None:
        #     instance.set_password(new_password)

        instance.save()
        return instance


class ChangeUserPasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    new_password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    email = serializers.CharField(max_length=255, read_only=True)
    result = serializers.CharField(read_only=True)

    def validate(self, data):
        old_password = data.get('old_password', None)
        new_password = data.get('new_password', None)

        print('old_password', old_password)
        print('new_password', new_password)

        # Вызвать исключение, если не предоставлен старый пароль.
        if old_password is None:
            raise serializers.ValidationError('An old_password address is required to change password.')
        # Вызвать исключение, если не предоставлен новый пароль.
        if new_password is None:
            raise serializers.ValidationError('A new_password is required to change password.')

        email = self.context.get('user', None).email
        if email is None:
            raise serializers.ValidationError('Cannot parse email to change password.')

        # проверка, что предоставленные почта и пароль соответствуют какому-то юзеру в БД
        user = authenticate(username=email, password=old_password)

        # если пользователь с данными почтой/паролем не найден
        if user is None:
            raise serializers.ValidationError('A user with this email and password was not found.')
        # если юзер деактивирован или заблокирован.
        if not user.is_active:
            raise serializers.ValidationError('This user has been deactivated.')

        # возвращаем словарь проверенных данных
        return {
            'email': email,
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
        representation['result'] = 'Password was changed!'
        return representation


class GetTokenSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    token = serializers.CharField(max_length=255)

# class MoveToBlacklistTokenSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     token = serializers.CharField(max_length=255)

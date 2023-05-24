from rest_framework import serializers

from users.models import User


class UserRegister(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    confirm_password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = (
            'username', 'email', 'password', 'confirm_password', 'profile_image')
        extra_kwargs = {
            'email': {'required': True}
        }

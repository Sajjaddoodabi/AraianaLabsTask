from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView
from .serializers import UserRegisterSerializer, UserSerializer, ChangePasswordSerializer
from .models import User


class UserRegisterView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = User


class UserRetrieveView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User


class UserUpdateView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User


class UserChangePassword(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    queryset = User

from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, UpdateAPIView
from .serializers import UserRegisterSerializer, UserSerializer, ChangePasswordSerializer
from .models import User


class UserRegisterView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = User


class UserRetrieveAndUpdateView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User


class UserChangePassword(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    queryset = User

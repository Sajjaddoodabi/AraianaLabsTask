from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from .serializers import UserRegisterSerializer, UserSerializer
from .models import User


class UserRegisterView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = User


class UserRetrieveAndUpdateView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User

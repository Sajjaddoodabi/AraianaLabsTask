from rest_framework.generics import CreateAPIView
from .serializers import UserRegisterSerializer
from .models import User


class UserRegisterView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = User

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserFollowingsSerializer, UserFollowersSerializer


class FollowView(APIView):
    def post(self, request, username):
        user = request.user

        if user.is_anonymous:
            raise AuthenticationFailed('unauthenticated!')

        following_user = User.objects.get(username=username)
        if not following_user:
            response = {'detail': 'user NOT found!'}
            return Response(response)

        if following_user not in user.followings.all():
            following_user.followers.add(user)
            user.followings.add(following_user)
            following_user.save()
            user.save()
        else:
            response = {'detail': f'already followed {following_user}'}
            return Response(response)

        response = {'detail': f'successfully followed {following_user}'}
        return Response(response)


class UnFollowView(APIView):
    def post(self, request, username):
        user = request.user

        if user.is_anonymous:
            raise AuthenticationFailed('unauthenticated!')

        unfollowing_user = User.objects.get(username=username)
        if not unfollowing_user:
            response = {'detail': 'user NOT found!'}
            return Response(response)

        if unfollowing_user in user.followings.all():
            unfollowing_user.followers.remove(user)
            user.followings.remove(unfollowing_user)
            unfollowing_user.save()
            user.save()
        else:
            response = {'detail': f'you do not follow {unfollowing_user}'}
            return Response(response)

        response = {'detail': f'successfully unfollowed {unfollowing_user}'}
        return Response(response)


class FollowingsListView(RetrieveAPIView):
    serializer_class = UserFollowingsSerializer
    queryset = User.objects.all()

    def get_object(self):
        user = self.request.user
        if user.is_anonymous:
            raise AuthenticationFailed('unauthenticated!')
        return user


class FollowersListView(RetrieveAPIView):
    serializer_class = UserFollowersSerializer
    queryset = User.objects.all()

    def get_object(self):
        user = self.request.user
        if user.is_anonymous:
            raise AuthenticationFailed('unauthenticated!')
        return user


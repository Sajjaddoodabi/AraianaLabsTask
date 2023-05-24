from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from .serializers import TweetSerializer
from .models import Tweet


class TweetsView(viewsets.ModelViewSet):
    serializer_class = TweetSerializer
    queryset = Tweet.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FollowingTweets(ListAPIView):
    serializer_class = TweetSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Tweet.objects.filter(user__in=user.followings.all())

from django.urls import path, include
from rest_framework import routers

from .views import TweetsView, FollowingTweets

router = routers.DefaultRouter()
router.register('tweet', TweetsView)

urlpatterns = [
    path('', include(router.urls)),
    path('following_tweets/', FollowingTweets.as_view(), name='followings_tweets'),
]

from django.urls import path, include
from rest_framework import routers

from .elastic import SearchTweets, AddTweetsToElastic, ClearElastic
from .views import TweetsView, FollowingTweets, SendMailToAll

router = routers.DefaultRouter()
router.register('tweet', TweetsView)

urlpatterns = [
    path('', include(router.urls)),
    path('following_tweets/', FollowingTweets.as_view(), name='followings_tweets'),
    path('send_mail/', SendMailToAll.as_view(), name='mail'),
    path('search/', SearchTweets.as_view(), name='search'),
    path('add_to_elastic/', AddTweetsToElastic.as_view(), name='add_to_elastic'),
    path('clear_elastic/', ClearElastic.as_view(), name='clear_elastic'),
]

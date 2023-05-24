from django.urls import path
from .views import *

urlpatterns = [
    path('follow/<str:username>/', FollowView.as_view(), name='follow'),
    path('unfollow/<str:username>/', UnFollowView.as_view(), name='follow'),
    path('followings/', FollowingsListView.as_view(), name='following'),
    path('followers/', FollowersListView.as_view(), name='followers'),
]

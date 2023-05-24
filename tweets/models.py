from django.db import models

from users.models import User


class Tweet(models.Model):
    parent = models.ForeignKey('self', null=True, on_delete=models.SET_NULL, related_name='retweets')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets', null=True)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

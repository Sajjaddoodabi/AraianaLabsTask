from django.db import models

from users.models import User


class FollowingList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    following = models.ManyToManyField(User, blank=True, related_name='followings')

    def __str__(self):
        return self.user.username

    def follow(self, user):
        if user in self.following.all():
            self.following.add(user)

    def unfollow(self, user):
        if user in self.following.all():
            self.following.remove(user)

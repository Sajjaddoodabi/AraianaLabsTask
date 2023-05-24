from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    retweets_count = serializers.SerializerMethodField()
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Tweet
        fields = ('id', 'user', 'parent', 'content', 'created_at', 'edited_at', 'retweets_count')
        read_only_fields = ('id', 'created_at', 'edited_at', 'user')
        extra_kwargs = {
            'content': {
                'error_messages': {
                    'max_length': "Tweet content is too Long"
                }
            }
        }

    @staticmethod
    def get_retweets_count(self):
        return self.retweets.count()



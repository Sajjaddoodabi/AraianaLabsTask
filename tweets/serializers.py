from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    # retweets_count = serializers.SerializerMethodField()
    # user = UserSerializer(read_only=True)

    class Meta:
        model = Tweet
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'edited_at')
        extra_kwargs = {
            'content': {
                'error_messages': {
                    'max_length': "Tweet content is too Long"
                }
            }
        }

    # def get_retweet_count(self):
    #     return self.retweets.count()



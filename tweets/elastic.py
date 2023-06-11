from elasticsearch import Elasticsearch
from rest_framework import serializers
from elasticsearch_dsl import Document, Text, Date, Search, Integer
from rest_framework.views import APIView

from AraianaLabsTask.local_settings import settings
from rest_framework.response import Response
from .models import Tweet

# Establish the Elasticsearch connection
es = Elasticsearch(
    hosts=settings["elk"]["hosts"],
    http_auth=(settings["elk"]["http_auth_username"], settings["elk"]["http_auth_password"]),
    scheme=settings["elk"]["scheme"],
    port=settings["elk"]["port"],
    use_ssl=settings["elk"]["use_ssl"],
    verify_certs=settings["elk"]["verify_certs"],
)


class TwitterSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    content = serializers.CharField(max_length=100)
    created_at = serializers.DateTimeField()


class TweetIndex(Document):
    id = Integer()
    content = Text()
    created_at = Date()

    class Index:
        name = 'tweets'

    @staticmethod
    def create_tweet(instance):
        tweet_index = TweetIndex(
            id=instance.id,
            content=instance.content,
            created_at=instance.created_at
        )

        tweet_index.save(using='default')

    @staticmethod
    def update_tweet(instance):
        tweet_index = TweetIndex.get(id=instance.id)
        tweet_index.content = instance.content
        tweet_index.save()

    @staticmethod
    def delete_tweet(instance):
        tweet_index = TweetIndex.get(id=instance.id)
        tweet_index.delete()

    @staticmethod
    def exists(tweet_id, **kwargs):
        exists = Search(index="tweets").query("match", id=tweet_id)
        exists.execute()

        if exists.count() == 0:
            return False
        else:
            return True


class SearchTweets(APIView):
    def get(self, request):
        query = request.GET.get("q", "")
        if query:
            tweets = Search(index="tweets").query("wildcard", content=f"*{query}*")
            search = tweets.execute()

            data = TwitterSerializer(search.hits, many=True).data
            return Response(data)
        return Response({"error": "No query provided"})


class AddTweetsToElastic(APIView):
    def post(self, request):
        tweets = Tweet.objects.all()
        for tweet in tweets:
            if TweetIndex.exists(tweet_id=tweet.id):
                continue
            TweetIndex.create_tweet(tweet)

        return Response({"success": "Tweets added to Elasticsearch"})


class ClearElastic(APIView):
    def delete(self, request):
        es.delete_by_query(index='tweets', body={"query": {"match_all": {}}})
        return Response({"success": "Elasticsearch cleared"})

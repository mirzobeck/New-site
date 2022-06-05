from rest_framework import serializers
from blog.models import post
from django.contrib.auth.models import User

class postserializers(serializers.ModelSerializer):
    cate = serializers.SlugRelatedField(slug_field='name', read_only=True)
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    class Meta:
        model = post
        fields = ['title', 'slug', 'author', 'cate', 'body', 'photo', 'publish','created', 'updated','status']


class userserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
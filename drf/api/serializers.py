from rest_framework import serializers
from blog.models import Article
from django.contrib.auth import get_user_model

User = get_user_model()

class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class UsersSerializers(serializers.ModelSerializer):
    # author = ArticleSerializers(read_only=True, many=True)
    class Meta:
        model = User
        fields = "__all__"
from django.shortcuts import render
from .serializers import ArticleSerializers, UsersSerializers
from blog.models import Article
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAdminUser
from .permissions import IsSuperUser, IsSuperUSerOrReadOnly, IsAuthorOrReadOnly
from django.contrib.auth import get_user_model

User = get_user_model()



class ArticleApiView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers


class ArticleDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    permission_classes = [IsAuthorOrReadOnly]

class UsersApiView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializers
    permission_classes = [IsAdminUser]
    
class UsersDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializers
    permission_classes = [IsAdminUser]

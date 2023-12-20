from django.shortcuts import render
from .serializers import ArticleSerializers
from blog.models import Article
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, ListCreateAPIView



class ArticleApiView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    

from django.shortcuts import render
from django.views.generic import ListView
from .models import Article

# Create your views here.


class ArticleViews(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(status=True)
        return query
from django.urls import path
from . import views


urlpatterns = [
    path ('', views.ArticleApiView.as_view()),
    path ('<int:pk>', views.ArticleDetailApiView.as_view()),
    path ('users/', views.UsersApiView.as_view()),
    path ('users/<int:pk>', views.UsersDetailApiView.as_view()),
]
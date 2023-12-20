from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.title
from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.name


class Post(models.Model):

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_posts')


class Like(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='liked_posts')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, related_name='likes')

    class Meta:
        unique_together = ('user', 'post')




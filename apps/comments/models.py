from django.db import models
from django.conf import settings
from apps.posts.models import Post

class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comments")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.SET_NULL,
    null=True, related_name="user_comments")


    def __str__(self) -> str:
        return self.text[:50]




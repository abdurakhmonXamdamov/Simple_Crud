from rest_framework import serializers 
from .models import Comment
from apps.posts.models import Post

class CommentSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)
    post = serializers.StringRelatedField(read_only=True)

    post_id = serializers.PrimaryKeyRelatedField(
        queryset = Post.objects.all(),
        source = 'post',
        write_only = True,
    )

    class Meta:
        model = Comment 
        fields = ['id', 'text', 'user', 'post', 'created_at', 'updated_at', 'deleted_at']



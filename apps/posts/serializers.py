from rest_framework import serializers
from .models import Category, Post, Like

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)

    category_id = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(),
        source = 'category',
        write_only = True,
    )

    user = serializers.StringRelatedField(read_only=True)
    like_count = serializers.SerializerMethodField()
    
    def get_like_count(self, obj):
        return obj.likes.count()

    class Meta:
        model = Post 
        fields = ['id', 'title', 'content', 'slug', 'category', 'category_id', 'user', 'like_count', 'created_at', 'updated_at']

        read_only_fields = ['id', 'created_at', 'updated_at']

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Like 
        fields = ['id', 'user', 'post']
        
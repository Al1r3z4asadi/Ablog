from rest_framework import serializers
from app_blog.models import *

class SingleArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'image', 'content', 'created_at')

class SumbitArticleSerializer(serializers.Serializer):
    title = serializers.CharField(required=True , allow_null=False , allow_blank=False , max_length=128)
    # image = serializers.FileField(required=True , allow_null=False )
    content = serializers.CharField(required=True , allow_null=False , allow_blank=False , max_length=528)
    category_id = serializers.IntegerField(required=True , allow_null=False )
    author_id = serializers.IntegerField(required=True , allow_null = False) 

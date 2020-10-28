from rest_framework import serializers
from app_blog.models import *

class SingleArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'image', 'content', 'created_at')
from django.shortcuts import render
from rest_framework.views import APIView
from app_blog.models import *
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class AllArticlesAPIView(APIView):

    def get(self , request , format=None):
        try:
            all_articles = Article.objects.all().order_by('-created_at')
            data = []
          
            for article  in all_articles :
                data.append(
                    {
                    'title': article.title ,
                    'cover': article.image.url , 
                    'category': article.category.title,
                    'created_at': article.created_at.date(),
                    }
                )
            context = {
                'articles_data':data,
            }

            return Response(data=data , status=status.HTTP_200_OK)

        except expression as identifier:
            return Response({'Error':status.HTTP_500_INTERNAL_SERVER_ERROR})
from django.shortcuts import render
from rest_framework.views import APIView
from app_blog.models import *
from rest_framework.response import Response
from rest_framework import status
from .serializers import SingleArticleSerializer
from django.db.models import Q

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


class SingleArticleAPIView(APIView):
    def get(self , request , format=None):

        try:
            print("print the request GET dictionary and fuck you bitch")
            print(request.GET)
            article_title = request.GET['article_title']
            the_article = Article.objects.filter(title__contains=article_title)
            serializer = SingleArticleSerializer(the_article, many=True)
            data =  serializer.data
            return Response(data=data , status=status.HTTP_200_OK)
        
        except expression as identifier:
            return Response({'Error':status.HTTP_500_INTERNAL_SERVER_ERROR})


class SearchArticleAPIView(APIView):
    
    def get(self , request , format=None):

        try:
            query = request.GET['query']
            articles = Article.objects.filter(Q(title__icontains=query))
            serializer = SingleArticleSerializer(articles , many = True)
            data = serializer.data
            return Response(data=data , status=status.HTTP_200_OK)
        except expression as identifier:
            return Response({'Error' :status.HTTP_500_INTERNAL_SERVER_ERROR})









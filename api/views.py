from django.shortcuts import render
from rest_framework.views import APIView
from app_blog.models import *
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import SingleArticleSerializer
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

# Create your views here.


# get users















class AllArticlesAPIView(APIView):
    
    permission_classes = [permissions.AllowAny]
    @method_decorator(cache_page(60*10))
    def get(self , request , format=None):
        try:
            print("printing the request.user and fuck you idiot hehe")
            print(request.user)
            print("printing the request.auth and fuck you u fucking moran")
            print(request.auth)
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

    permission_classes = [permissions.AllowAny]    
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
    
    permission_classes = [permissions.AllowAny]
    @method_decorator(cache_page(60*10))
    def get(self , request , format=None):

        try:
            query = request.GET['query']
            articles = Article.objects.filter(Q(title__icontains=query))
            serializer = SingleArticleSerializer(articles , many = True)
            data = serializer.data
            return Response(data=data , status=status.HTTP_200_OK)
        except expression as identifier:
            return Response({'Error' :status.HTTP_500_INTERNAL_SERVER_ERROR})




# class SubmitArticleAPIView(APIView):

#     def post(self , request , format=None):

#         try:
#             pass
#         except expression as identifier:
#             pass







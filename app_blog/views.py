from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
# Create your views here.

class IndexPage(TemplateView):

    def get(self , request , **kwargs):

        articles_data = []
        all_articles = Article.objects.all()[:9]
        for article  in all_articles :
            articles_data.append(
                {
                'title': article.title ,
                'cover': article.image.url , 
                'category': article.category.title,
                'created_at': article.created_at.date(),
                }
            )
        context = {
            'articles_data':articles_data,
        }

        return render(request , 'app_blog/index.html' , context)
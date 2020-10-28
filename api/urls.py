from django.urls import path
from . import views as api_view


urlpatterns = [
    path('v1/article/' , api_view.SingleArticleAPIView.as_view() , name='single_article'),
    path('v1/article/all/', api_view.AllArticlesAPIView.as_view() , name='all_articles'),
    path('v1/article/search/' , api_view.SearchArticleAPIView.as_view() , name='search_article')

]

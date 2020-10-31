from django.urls import path , include
from . import views as api_view



urlpatterns = [
    path('v1/article/' , api_view.SingleArticleAPIView.as_view() , name='single_article'),
    path('v1/article/all/', api_view.AllArticlesAPIView.as_view() , name='all_articles'),
    path('v1/article/search/' , api_view.SearchArticleAPIView.as_view() , name='search_article'),
    path('v1/article/submit/' , api_view.SubmitArticleAPIView.as_view() , name='submit_article'),
    path('auth/' , include('djoser.urls')),
    path('auth/' , include('djoser.urls.authtoken')),
    

]

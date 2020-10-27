from django.urls import path
from . import views as api_view


urlpatterns = [
   path('v1/article/all/', api_view.AllArticlesAPIView.as_view() , name='all_articles'),

]

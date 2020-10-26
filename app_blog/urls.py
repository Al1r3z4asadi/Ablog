from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app_blog import views as blog_view

urlpatterns = [
   path('', blog_view.IndexPage.as_view() , name='home'),
]

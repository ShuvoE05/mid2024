# urls.py
from django.urls import path
from .views import create_blog_post

urlpatterns = [
    path('create/', create_blog_post, name='create_blog_post'),
]

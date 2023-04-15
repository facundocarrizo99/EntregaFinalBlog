from django.urls import path
from .views import createPost, createComment, postHome, onePost, home

from LogInApp.views import *

urlpatterns = [
    path('addPosts', createPost, name="CreatePost"),
    path('addComment', createComment, name="CreateComment"),
    path('allPosts', postHome, name="AllPosts"),
    path('post', onePost, name="OnePost"),
    path('', home, name="Home"),
]
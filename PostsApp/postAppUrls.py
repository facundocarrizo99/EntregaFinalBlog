from django.urls import path
from .views import home, CreatePost, PostDetails, UpdatePost, DeletePost, HomeView, AboutUs
from accounts.views import *

urlpatterns = [
    path('', HomeView.as_view(), name="Home"),
    path('addPost/', CreatePost.as_view(), name="PostCreate"),
    path('post/<int:pk>', PostDetails.as_view(), name="PostDetail"),
    path('post/edit/<int:pk>', UpdatePost.as_view(), name="PostUpdate"),
    path('post/delete/<int:pk>', DeletePost.as_view(), name="PostDelete"),
    path('aboutus/', AboutUs.as_view(), name="AboutUs"),
]
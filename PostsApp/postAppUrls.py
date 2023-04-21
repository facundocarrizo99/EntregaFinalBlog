from django.urls import path
from .views import createComment, home

from LogInApp.views import *

urlpatterns = [
    path('', home, name="Home"),
    path('addComment', createComment, name="CreateComment"),

]
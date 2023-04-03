from django.urls import path

from LogInApp.views import *

urlpatterns = [
    path('registro', CreateBlogger, name="CreateBlogger"),
    path('registroAdmin', CreateAdmin, name="CreateAdmin"),
]
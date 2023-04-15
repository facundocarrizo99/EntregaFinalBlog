from django.urls import path

from LogInApp.views import *

urlpatterns = [
    path('registro', createBlogger, name="CreateBlogger"),
    path('registroAdmin', createAdmin, name="CreateAdmin"),
    path('login', logInRequest, name="LogIn"),
    path('redirect', redirect, name="Redirect")
]
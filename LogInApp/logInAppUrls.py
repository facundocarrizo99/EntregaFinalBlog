from django.urls import path

from LogInApp.views import *

urlpatterns = [
    path('registro/', CreateBlogger.as_view(), name="CreateBlogger"),
]
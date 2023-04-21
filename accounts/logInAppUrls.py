from django.urls import path
from accounts.views import CreateBlogger

urlpatterns = [
    path('registro/', CreateBlogger.as_view(), name="CreateBlogger"),
]
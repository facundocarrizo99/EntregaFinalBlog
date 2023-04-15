from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from LogInApp.models import Blogger

class CustomBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        Blogger = get_user_model()

        try:
            user = Blogger.objects.get(username=username)
            if Blogger.check_password(password):
                return user
        except Blogger.DoesNotExist:
            return None

    def get_user(self, user_id):
        Blogger = get_user_model()

        try:
            return Blogger.objects.get(pk=user_id)
        except Blogger.DoesNotExist:
            return None

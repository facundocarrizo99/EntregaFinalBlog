from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.
class CreateBlogger(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registroBlogger.html'
    success_url = reverse_lazy('login')

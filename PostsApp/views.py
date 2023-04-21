from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import PostForm, CommentForm, BusquedaCommentForm, BusquedaPostForm, PostEditForm
from .models import Post, Comment

# Create your views here.
def home(request):
    return render(request, "PostViews/home.html", {})

class HomeView(ListView):
    model = Post
    template_name = 'PostViews/home.html'
    ordering = ['-postDate']

class CreatePost(CreateView):
    model = Post
    form = PostForm
    template_name = 'PostViews/postCreate.html'

class PostDetails(CreateView):
    model = Post
    template_name = 'PostViews/postDetails.html'

class UpdatePost(CreatePost):
    model = Post
    form = PostEditForm
    template_name = 'PostViews/postUpdate.html'

class DeletePost(CreatePost):
    model = Post
    template_name = 'PostViews/postDelete.html'
    success_url = reverse_lazy('Home')



#@login_required(login_url="LogInViwes/logIn.html")
def createComment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            owner = form.cleaned_data['commentOwner']
            postAsosiado = form.cleaned_data["post"]
            text = form.cleaned_data["texto"]
            fecha = datetime.now()
            t = Comment(commentOwner=owner, post=postAsosiado, texto=text, fecha=fecha)
            t.save()
    context = {
        "form": CommentForm()
    }
    return render(request, "PostViews/createComment.html", context=context)




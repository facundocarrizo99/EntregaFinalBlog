from django.shortcuts import render
from datetime import datetime
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import PostForm, CommentForm, PostEditForm
from .models import Post, Comment


# Create your views here.
def home(request):
    return render(request, "PostViews/home.html", {})

class HomeView(ListView):
    model = Post
    template_name = 'PostViews/home.html'
    ordering = ['-postDate']

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        return context


class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'PostViews/postCreate.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(CreatePost, self).get_context_data(*args, **kwargs)
        return context


class PostDetails(DetailView):
    model = Post
    fields = '__all__'
    template_name = 'PostViews/postDetails.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetails, self).get_context_data(*args, **kwargs)
        return context


class UpdatePost(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'PostViews/postUpdate.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(UpdatePost, self).get_context_data(*args, **kwargs)
        return context


class DeletePost(DeleteView):
    model = Post
    template_name = 'PostViews/postDelete.html'
    success_url = reverse_lazy('Home')

    def get_context_data(self, *args, **kwargs):
        context = super(DeletePost, self).get_context_data(*args, **kwargs)
        return context

class AboutUs(CreateView):
    model = Post
    fields = '__all__'
    template_name = 'PostViews/aboutUs.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AboutUs, self).get_context_data(*args, **kwargs)
        return context


# @login_required(login_url="LogInViwes/logIn.html")
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
        "form_class": CommentForm()
    }
    return render(request, "PostViews/createComment.html", context=context)

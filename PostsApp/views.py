from django.shortcuts import render
from .forms import PostForm, CommentForm, BusquedaCommentForm, BusquedaPostForm
from .models import Post, Comment

# Create your views here.
def createPost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            mail = form.cleaned_data["userEmail"]
            username = form.cleaned_data["userName"]
            password = form.cleaned_data["userPassword"]
            t = Admin(userEmail=mail, userName=username, userPassword=password)
            t.save()
    context = {
        "form": AdminForm()
    }
    return render(request, "LogInViews/registroAdmin.html", context=context)


def createComment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            mail = form.cleaned_data["userEmail"]
            username = form.cleaned_data["userName"]
            password = form.cleaned_data["userPassword"]
            t = Admin(userEmail=mail, userName=username, userPassword=password)
            t.save()
    context = {
        "form": AdminForm()
    }
    return render(request, "LogInViews/registroAdmin.html", context=context)


def postHome(request):
    all_posts = Post.objects.all()
    context = {
        "posts": all_posts,
        "form_busqueda": BusquedaPostForm(),
    }
    return render(request, "posts.html", context=context)


def onePost(request):
    one_post = Post.objects.only() #To Do: verificar que post trae, que no sea cualquiera
    context = {
        "posts": one_post,
        "form_busqueda": BusquedaPostForm(),
    }
    return render(request, "onePost.html", context=context)

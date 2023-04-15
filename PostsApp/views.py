from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .forms import PostForm, CommentForm, BusquedaCommentForm, BusquedaPostForm
from .models import Post, Comment

# Create your views here.
#@login_required(login_url="LogInViwes/logIn.html")
def createPost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["titulo"]
            subTitle = form.cleaned_data["subTitulo"]
            body = form.cleaned_data["cuerpo"]
            duenio = form.cleaned_data["owner"]
            fecha = datetime.now()
            #file = form.cleaned_data["foto"]
            t = Post(titulo=title, subTitulo=subTitle, cuerpo=body, owner=duenio, fecha=fecha)
            t.save()
    context = {
        "form": PostForm()
    }
    return render(request, "PostViews/createPost.html", context=context)


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


#@login_required(login_url="LogInViwes/logIn.html")
def postHome(request):
    all_posts = Post.objects.all()
    context = {
        "posts": all_posts,
        "form_busqueda": BusquedaPostForm(),
    }
    return render(request, "PostViews/posts.html", context=context)


#@login_required(login_url="LogInViwes/logIn.html")
def onePost(request):
    one_post = Post.objects.only() #To Do: verificar que post trae, que no sea cualquiera
    context = {
        "posts": one_post,
        "form_busqueda": BusquedaPostForm(),
    }
    return render(request, "PostViews/onePost.html", context=context)


def home(request):
    return render(request, "PostViews/home.html")
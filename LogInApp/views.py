from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .models import Blogger, Admin
from .forms import BloggerForm, AdminForm
from .customBackend import CustomBackend

# Create your views here.
def createBlogger(request):
    if request.method == "POST":
        form = BloggerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["nombre"]
            surname = form.cleaned_data["apellido"]
            mail = form.cleaned_data["email"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["userpassword"]
            t = Blogger(nombre=name, apellido=surname, email=mail, username=username, userpassword=password)
            t.save()
            return render(request, "PostViews/home.html")
    context = {
        "form": BloggerForm()
    }
    return render(request, "LogInViews/registroBlogger.html", context=context)


def createAdmin(request):
    if request.method == "POST":
        form = AdminForm(request.POST)
        if form.is_valid():
            mail = form.cleaned_data["email"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["userpassword"]
            t = Admin(email=mail, username=username, userpassword=password)
            t.save()
            return render(request, "PostViews/home.html")
    context = {
        "form": AdminForm()
    }
    return render(request, "LogInViews/registroAdmin.html", context=context)


def logInRequest(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')
            return render(request, 'PostViews/posts.html')
            """
            user = CustomBackend(request, username=usuario, password=clave)

            if user not in None:
                login(request, user)
                return redirect('AllPosts')
            else:
                error_message = 'Invalid username or password'
                return render(request, 'LogInViews/logIn.html', {'error_message': error_message})
                """
        else:
            return render(request, "PostViews/home.html", {"mensaje": f"Formulario incorrecto"})

    form = AuthenticationForm()
    return render(request, "LogInViews/logIn.html", {'form':form})
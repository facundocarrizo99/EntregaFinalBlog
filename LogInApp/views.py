from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from .models import Blogger, Admin
from .forms import BloggerForm, AdminForm

# Create your views here.
def createBlogger(request):
    if request.method == "POST":
        form = BloggerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["nombre"]
            surname = form.cleaned_data["apellido"]
            mail = form.cleaned_data["userEmail"]
            username = form.cleaned_data["userName"]
            password = form.cleaned_data["userPassword"]
            t = Blogger(nombre=name, apellido=surname, userEmail=mail, userName=username, userPassword=password)
            t.save()
    context = {
        "form": BloggerForm()
    }
    return render(request, "LogInViews/registroBlogger.html", context=context)


def createAdmin(request):
    if request.method == "POST":
        form = AdminForm(request.POST)
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


def logInRequest(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=clave)

            if user not in None:
                login(request, user)
                return render(request, "LogInViews/homeScreenLogged.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "LogInViews/homeScreenLogged.html", {"mensaje": f"Error, Datos incorrectos"})
        else:
            return render(request, "LogInViews/homeScreenLogged.html", {"mensaje": f"Formulario incorrecto"})

    form = AuthenticationForm()
    return render(request, "LogInViews/registroAdmin.html", {'form':form})
from django.shortcuts import render
from .models import Blogger, Admin
from .forms import BloggerForm, AdminForm

# Create your views here.
def CreateBlogger(request):
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


def CreateAdmin(request):
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
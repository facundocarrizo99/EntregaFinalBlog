from django.db import models
from LogInApp.models import Blogger

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=128)
    subTitulo = models.CharField(max_length=256)
    cuerpo = models.CharField(max_length=1024)
    owner = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    fecha = models.DateTimeField
    foto = models.FileField


class Comment(models.Model):
    commentOwner = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    texto = models.CharField(max_length=150)
    fecha = models.DateTimeField

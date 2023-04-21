
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=128)
    subTitulo = models.CharField(max_length=256)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo = models.TextField()
    postDate = models.DateTimeField(auto_now_add=True)
    foto = models.FileField()

    def __str__(self):
        return self.titulo + ' | ' + str(self.owner)

    def getConstantURL(self):
        return reverse('OnePost', args=(str(self.id)))

class Comment(models.Model):
    commentOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    texto = models.CharField(max_length=150)
    commentDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post + ' | ' + str(self.commentOwner)

    def getConstantURL(self):
        return reverse('Home')
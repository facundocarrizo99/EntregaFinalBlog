from datetime import datetime

from django.db import models
from LogInApp.models import Blogger

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=128)
    subTitulo = models.CharField(max_length=256)
    cuerpo = models.CharField(max_length=1024)
    owner = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=datetime.now())
    foto = models.FileField()

    def __str__(self):
        return f"titulo: {self.titulo}, subTitulo: {self.subTitulo}, cuerpo: {self.cuerpo}, owner: {self.owner}, fecha: {self.fecha}, foto: {self.foto}"

class Comment(models.Model):
    commentOwner = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    texto = models.CharField(max_length=150)
    fecha = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"commentOwner: {self.commentOwner}, post: {self.post}, texto: {self.texto}, fecha: {self.fecha}"

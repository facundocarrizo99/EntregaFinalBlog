from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=128)
    subTitulo = models.CharField(max_length=256)
    cuerpo = models.CharField(max_length=1024)
    autor = models.ForeignKey()#To Do ver como linkea con un blogger en la BD
    fecha = models.DateTimeField
    foto = models.FileField


from django.db import models

# Create your models here.
class Account(models.Model):
    userName = models.CharField(max_length=20)
    userEmail = models.EmailField()
    userPassword = models.CharField(max_length=20)

    def __str__(self):
        return f"Usuario: {self.userName}, Email: {self.userEmail}, Password: {self.userPassword}"


class Blogger(Account):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}"


class Admin(Account):
    def fullPower(self):
        print("nothing yet")
        #tiene mas poder pero no se si me interesa saber mas de el. TBD
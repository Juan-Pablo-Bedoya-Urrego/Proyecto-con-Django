from django.db import models

# Create your models here.
class Register(models.Model):
    email = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

class Servicios(models.Model):
    nombreProducto = models.CharField(max_length=250)
    descripcionProducto = models.CharField(max_length=250)
    precioProducto = models.CharField(max_length=250)
    imagenProducto = models.ImageField(upload_to='servicios')
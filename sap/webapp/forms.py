from django import forms
from productos.models import Register

class formRegistro(forms.Form):
    email = forms.EmailField(label='Email:', required=True)
    name = forms.CharField(max_length=250, label='Nombre:', required=True)
    lastname = forms.CharField(max_length=250, label='Apellidos:', required=True)
    username = forms.CharField(max_length=250,label='Nombre de usuario:', required=True)
    password = forms.CharField(max_length=250, label='Contraseña:' ,required=True)

class formLogin(forms.Form):
    username = forms.CharField(max_length=250,label='Nombre de usuario:', required=True)
    password = forms.CharField(max_length=250, label='Contraseña:' ,required=True)

class ServicioForm(forms.Form):
    nombreProducto = forms.CharField(max_length=250, label= 'Nombre del producto', required=True)
    descripcionProducto = forms.CharField(max_length=250, label= 'Descripcion del producto', required=True)
    precioProducto = forms.CharField(max_length=250, label= 'Precio del producto', required=True)
    imagenProducto = forms.ImageField(label='Imagen del producto', required=True)
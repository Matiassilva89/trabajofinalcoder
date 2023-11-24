from django import forms
from django.contrib.auth.forms import UserChangeForm

from django.contrib.auth.models import User


    
  #trabaja con nosotros  
class Trabajaconnos(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    edad = forms.IntegerField()
    
#contacto
     
class Contactoform(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
 
#consulta de numero de pedido    
class Pedidoform(forms.Form):
    numero = forms.CharField()
    dni = forms.CharField()
    
#Agregar pedido    
class Agregarpedidoform(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    detallar = forms.CharField()
    cantidad = forms.IntegerField()
    
 #editar perfil   
    
class UserEditForm(UserChangeForm):
   
    password = None
    email = forms.EmailField(label="Ingrese su email:")
    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre')
    imagen = forms.ImageField(label="Avatar", required=False)
    descripcion = forms.CharField(required=False)
    link = forms.URLField(required=False)
    
    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name', 'imagen', 'descripcion','link']
        
        
from django.db import models
from django.contrib.auth.models import User

   
#trabaja con nosotros   
class Personal2(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    edad = models.IntegerField()
    
    
#contacto   
class Contacto(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    
 #estado de tu pedido
 
class Pedido(models.Model):
    numero = models.IntegerField()
    dni = models.IntegerField()
    
 #agregar pedido

class Agregarpedido(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    detallar = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    
#avatar

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
    descripcion = models.TextField(null=True)
    link = models.URLField(null=True)
    
    def __str__(self):
        return f"{self.user} - {self.imagen}"
    
    
    
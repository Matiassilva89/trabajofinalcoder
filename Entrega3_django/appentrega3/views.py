from django.shortcuts import render
from django.http import HttpResponse
from appentrega3.models import Personal2, Contacto, Pedido, Agregarpedido, Avatar
from appentrega3.forms import Trabajaconnos , Contactoform, Pedidoform, Agregarpedidoform, UserEditForm

from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView ,UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


from django.core.files import File






# inicio

def inicio(request):
    return render(request, 'appentrega3/index.html')


#trabaja con nosotros
def trabajaconnos(request):
    if request.method == 'POST':
        miFormulario = Trabajaconnos(request.POST) #<- traigo del template los datos de los input
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            info = Personal2(nombre = info['nombre'], apellido = info['apellido'], email = info['email'],edad = info['edad']) #viene de models
            info.save()
            return render(request, 'appentrega3/graciaspersonal.html')
    else:
        miFormulario = Trabajaconnos()
    return render(request, "appentrega3/trabajaconnosotros.html",{'miFormulario':miFormulario})

#contacto

def contactoform(request):
    if request.method == 'POST':
        miFormulario = Contactoform(request.POST) #<- traigo del template los datos de los input
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            info = Contacto(nombre = info['nombre'], apellido = info['apellido'], email = info['email'])
            info.save()
            return render(request, 'appentrega3/graciascontacto.html')
    else:
        miFormulario = Contactoform()
    return render(request, "appentrega3/contactoform.html",{'miFormulario':miFormulario})

#Numero de pedido

@login_required
def pedidoform(request):
    if request.method == 'POST':
        miFormulario = Pedidoform(request.POST) #<- traigo del template los datos de los input
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            info = Pedido(numero = info['numero'], dni = info['dni'])
            info.save()
            return render(request, 'appentrega3/graciaspedido.html')
    else:
        miFormulario = Pedidoform()
    return render(request, "appentrega3/pedidoform.html",{'miFormulario':miFormulario})

#Agregar pedido


def agregarpedidoform(request):
    if request.method == 'POST':
        miFormulario = Agregarpedidoform(request.POST) #<- traigo del template los datos de los input
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            agregarpedido = Agregarpedido(nombre = info['nombre'], apellido = info['apellido'], email = info['email'], detallar = info['detallar'],cantidad = info['cantidad'] )
            agregarpedido.save()
            return render(request, 'appentrega3/index.html')
    else:
        miFormulario = Agregarpedidoform()
    return render(request, "appentrega3/agregarpedidoform.html",{'miFormulario':miFormulario})

#gracias

def graciaspedido(request):
    return render(request, 'appentrega3/graciaspedido.html')

def graciaspersonal(request):
    return render(request, 'appentrega3/graciaspersonal.html')

def graciascontacto(request):
    return render(request, 'appentrega3/graciascontacto.html')

#index para otras vistas

def nuevoindex(request):
    return render(request, 'appentrega3/nuevoindex.html')

#acerca de  mi
def acercademi(request):
    return render(request, 'appentrega3/acercademi.html')

#nosotros

def sobrenosotros(request):
    return render(request, 'appentrega3/sobrenosotros.html')




#ver --- editar --- eliminar pedidos

class CursoListView(LoginRequiredMixin,ListView):
    model = Agregarpedido
    context_object_name = "pedidos"
    template_name = "appentrega3/pedidos_lista.html"


class CursoDetailView(LoginRequiredMixin,DetailView):
    model = Agregarpedido
    template_name = "appentrega3/pedidos_detalle.html"


class CursoCreateView(CreateView):
    model = Agregarpedido
    template_name = "appentrega3/pedidos_crear.html"
    success_url = reverse_lazy('ListaPedidos')
    fields = ['nombre','apellido','email','detallar','cantidad']


class CursoUpdateView(UpdateView):
    model = Agregarpedido
    template_name = "appentrega3/pedidos_editar.html"
    success_url = reverse_lazy('ListaPedidos')
    fields = ['nombre','apellido','email','detallar','cantidad']

class CursoDeleteView(DeleteView):
    model = Agregarpedido
    template_name = "appentrega3/pedidos_borrar.html"
    success_url = reverse_lazy('ListaPedidos')
    
    
#buscar pedidos

   
@login_required 
def buscar_pedidos(request):
    query = request.GET.get('q')
    if query:
        results = Agregarpedido.objects.filter(apellido__icontains=query)
    else: #si hacemos click al botón sin datos!!!!
        results = []
    
    return render(request, 'appentrega3/buscar_pedidos.html', {'results': results})


#Inicias sesion

def login_view(request):

    if request.method == "POST": #click al boton iniciar sesion

        form_inicio = AuthenticationForm(request, data = request.POST)
        
        if form_inicio.is_valid(): #el formulario nos ayuda a validar

            info = form_inicio.cleaned_data #data que se escribio en el formulario de login en modo diccionario 
            usuario = info.get("username")
            contra = info.get("password")

            #acá hacemos la validación
            user = authenticate(username=usuario, password=contra) #existe el usuario (retorna el usuario) ---- no existe usuario (retorna None)

            if user:
                login(request, user)    #iniciar sesion ya que el usuario si existe (credenciales correctas)
                return render(request, "appentrega3/index.html", {"usuario":user})
        
        else:
            return render(request,"appentrega3/index.html", {"mensaje":"DATOS INCORRECTOS"})

    form_inicio = AuthenticationForm() #formulario vacio

    return render(request,"appentrega3/login.html", {"form":form_inicio} )


#Registro

def register(request):
    if request.method == 'POST':
            form = UserCreationForm(request.POST)
            #form = UserRegisterForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                form.save()
                return render(request,"appentrega3/index.html" ,  {"mensaje":"Usuario Creado :)"})
    else:
            form = UserCreationForm()
            #form = UserRegisterForm()
    return render(request,"appentrega3/register.html" ,  {"form":form})



##editar perfil

@login_required
@login_required
def editarPerfil(request):
    usuario = request.user

    # Manejar solicitudes para favicon.ico
    if request.path == '/favicon.ico/':
        return HttpResponseNotFound()

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES, instance=request.user)
        if miFormulario.is_valid():
            if hasattr(usuario, 'avatar') and usuario.avatar:
                if miFormulario.cleaned_data.get('imagen'):
                    usuario.avatar.imagen = miFormulario.cleaned_data.get('imagen')
                    usuario.avatar.save()
                else:
                    # Si no se proporciona una imagen, establece una imagen por defecto
                    imagen_por_defecto = 'media/avatares/nonavatar.png'
                    with open(imagen_por_defecto, 'rb') as f:
                        usuario.avatar.imagen.save('imagen_por_defecto.jpg', File(f))
            else:
                # Si el usuario no tiene un avatar, crea uno y guarda la imagen
                avatar = Avatar.objects.create(user=usuario)
                if miFormulario.cleaned_data.get('imagen'):
                    avatar.imagen = miFormulario.cleaned_data.get('imagen')
                    avatar.save()
                else:
                    # Si no se proporciona una imagen, establece una imagen por defecto
                    imagen_por_defecto = 'media/avatares/nonavatar.png'
                    with open(imagen_por_defecto, 'rb') as f:
                        avatar.imagen.save('imagen_por_defecto.jpg', File(f))

            miFormulario.save()
            return render(request, "appentrega3/index.html")
    else:
        # Si el usuario no tiene avatar, crea uno y establece la imagen por defecto en el formulario
        if not hasattr(usuario, 'avatar') or not usuario.avatar:
            avatar = Avatar.objects.create(user=usuario)
            imagen_por_defecto = 'media/avatares/nonavatar.png'
            with open(imagen_por_defecto, 'rb') as f:
                avatar.imagen.save('imagen_por_defecto.jpg', File(f))

        miFormulario = UserEditForm(initial={'imagen': usuario.avatar.imagen}, instance=request.user)

    return render(request, "appentrega3/editar_perfil.html", {"miFormulario": miFormulario, "usuario": usuario})
class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = 'appentrega3/editar_contrasenia.html'
    success_url = reverse_lazy('editarPerfil')
    
    
    
  

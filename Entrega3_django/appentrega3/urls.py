from django.urls import path
from appentrega3.views import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

urlpatterns = [
    
    
   #Url de formularios 
    
    path('trabajaconnos/',trabajaconnos, name='trabajaconnos'),
    path('contactoform/',contactoform, name='contactoform'),
    path('pedidoform/',pedidoform, name='pedidoform'),
    path('agregarpedidoform/',agregarpedidoform, name='agregarpedidoform'),
    #Url otras paginas
    path('', inicio, name = "home"),
    path('graciaspedido/',graciaspedido, name='graciaspedido'),
    path('graciaspersonal/',graciaspersonal, name='graciaspersonal'),
    path('graciascontacto/',graciascontacto, name='graciascontacto'),
    path('nuevoindex/',nuevoindex, name='nuevoindex'),
    path('acercademi/', acercademi, name="acercademi"),
    path('sobrenosotros/', sobrenosotros, name="sobrenosotros"),
    
     #urls de búsqueda
    path('buscar_pedidos/',buscar_pedidos, name='buscar_pedidos'),
 
     #login
     
    path('login/', login_view, name="Login"),
    path('register/', register, name="Register"),
    path('logout/', LogoutView.as_view(template_name='appentrega3/logout.html'), name='Logout'),
    path('editarPerfil', editarPerfil, name="editarPerfil"), 
    path('cambiarContrasenia', CambiarContrasenia.as_view(), name="CambiarContrasenia"),
    
    #ver-editar-borrar
    path('lista/', CursoListView.as_view(), name = "ListaPedidos"),
    path('nuevo/', CursoCreateView.as_view(), name = "NuevoPedido"),
    path('<pk>/', CursoDetailView.as_view(), name = "DetallePedido"),
    path('<pk>/editar/', CursoUpdateView.as_view(), name = "EditarPedido"),
    path('<pk>/borrar/', CursoDeleteView.as_view(), name = "BorrarPedido"),
    
   
]
    
    

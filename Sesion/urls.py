from django.urls import path
from Sesion import views

urlpatterns = [
    path('', views.iniciarsesion, name = 'InicioSesion'),
    path('Registro/', views.registrar_cuenta, name = 'RegistroCuenta'),
    path('logout/', views.cerrar_sesion, name='CerrarSesion'),
    path('MiPerfil/', views.miperfil, name='MiPerfil'),
    path('MiPerfil/Editar', views.editar_perfil, name='EditarPerfil'),
    path('MiPerfil/CambiarContraseña', views.cambiar_contraseña, name='CambiarContraseña'),
]
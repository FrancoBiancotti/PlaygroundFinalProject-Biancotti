from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from Sesion.forms import FormularioInicio, FormularioRegistro

from Sesion.models import UserExtension
from Sesion.forms import FormularioRegistro, FormularioEditarPerfil, FormularioCambiarContraseña

def iniciarsesion (request):
    if request.user.is_authenticated:
        return redirect('Inicio')

    if request.method == 'POST':
        formulario_login = FormularioInicio(request, data=request.POST)
        if formulario_login.is_valid():
            user = formulario_login.get_user()
            login(request, user)
            user_extension, es_nuevo_userextension = UserExtension.objects.get_or_create(user=request.user)
            return redirect('Inicio')
    else:
        formulario_login = FormularioInicio()

    return render(request,'Sesion/inicio.html', { 'formulario_login' : formulario_login })

def registrar_cuenta(request):

# Sólo permite el ingreso si NO se está logueado. Caso contrario, redirige a 'home'
# Esta validación es útil cuando se intenta ingresar forzando la URL
    if request.user.is_authenticated:
        return redirect('Inicio')

    if request.method == 'POST':
        formulario_registro = FormularioRegistro(request.POST)
        print ("HOLA0")
        if formulario_registro.is_valid():
            print ("Hola")
            formulario_registro.save()
            return redirect('Inicio')
    else:
        formulario_registro = FormularioRegistro()

    return render(request, 'Sesion/registro.html', { 'formulario_registro' : formulario_registro })

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('Inicio')

@login_required
def miperfil(request):
    return render(request,'Sesion/miperfil.html')

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        formulario_editar_perfil = FormularioEditarPerfil(request.POST)

        if formulario_editar_perfil.is_valid():
            datos_perfil = formulario_editar_perfil.cleaned_data

            request.user.email = datos_perfil['email']
            request.user.first_name = datos_perfil['first_name']
            request.user.last_name = datos_perfil['last_name']
            request.user.userextension.descripcion = datos_perfil['descripcion']

            request.user.save()
            request.user.userextension.save()

            return redirect('MiPerfil')
    else:
        formulario_editar_perfil = FormularioEditarPerfil(
            initial={
                'email' : request.user.email,
                'first_name' : request.user.first_name,
                'last_name' : request.user.last_name,
                'descripcion' : request.user.userextension.descripcion,
            }
        )

    return render(request, 'Sesion/editar_perfil.html', { 'formulario_editar_perfil' : formulario_editar_perfil })

@login_required
def cambiar_contraseña(request):
    if request.method == 'POST':
        formulario_cambio_contraseña = FormularioCambiarContraseña(user=request.user, data=request.POST)

        if formulario_cambio_contraseña.is_valid():
            formulario_cambio_contraseña.save()
            update_session_auth_hash(request, request.user)
            return redirect('MiPerfil')
    else:
        formulario_cambio_contraseña = FormularioCambiarContraseña(user=request.user)

    return render(request, 'Sesion/cambiar_contraseña.html', { 'formulario_cambio_contraseña' : formulario_cambio_contraseña })

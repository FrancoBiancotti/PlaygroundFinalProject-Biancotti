from django.shortcuts import render, redirect
from django.db.models import Q
from Chat.models import Chat, Mensaje
from Sesion.models import UserExtension
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from Chat.forms import FormularioEnvioMensaje
from django.contrib.auth.models import User

@login_required
def chats (request):
    print (User)
    variable = User.objects.exclude(username=request.user)
    return render(request,'Chat/inicio.html',{"value" : variable})

# @login_required
# def chats_n2 (request, pk):
#     print (pk)
#     User = get_user_model()
#     variable = User.objects.exclude(username=request.user)
#     return render(request,'Chat/inicio.html',{"value" : variable})

@login_required
def chats_n(request, pk):
    print(pk)
    # chat = Chat.objects.all().delete()
    try: 
        chat = Chat.objects.all().filter(user_chat_2=request.user).union(
            Chat.objects.all().filter(user_chat_1=request.user)
    ).order_by('id')[0]
    except:
        chat = Chat(user_chat_1 = request.user,user_chat_2 = User.objects.get(id=pk))
    mensajes = None
# Esta vista disponibiliza la conversación con el usuario, y permite enviar un nuevo mensaje
    if request.method == 'POST':
        formulario_envio_mensaje = FormularioEnvioMensaje(request.POST)

        if formulario_envio_mensaje.is_valid():
            datos_mensaje = formulario_envio_mensaje.cleaned_data
            de_user = request.user
            chat.save()
            de_user.save()
            nuevo_mensaje = Mensaje(
                chat = chat,
                de_user = request.user,
                contenido = datos_mensaje['contenido']
            )
            nuevo_mensaje.save()
            return redirect('Chats')
    else:
        mensajes = Mensaje.objects.filter(chat=chat).order_by('id')

        formulario_envio_mensaje = FormularioEnvioMensaje()

    return render(request, 'Chat/chats_n.html', { 'formulario_envio_mensaje' : formulario_envio_mensaje, 'chat' : chat, 'mensajes' : mensajes, 'pk': pk })
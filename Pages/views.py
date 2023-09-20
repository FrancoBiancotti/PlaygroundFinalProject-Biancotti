from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from Pages import forms, models
from django.contrib.auth.models import User

from Pages.models import Post
from Pages.forms import FormularioCrearBlog
from django.contrib.auth.decorators import login_required

from django.views.generic import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test

# def posteos(request):
#     posts = Post.objects.all().order_by('id')
#     return render(request, 'Pages/posteos.html', { 'posts' : posts })
@login_required
def posteos (request):
    posts = Post.objects.all().order_by('id')
    if request.method == 'POST':
        formulario_crear_blog = forms.FormularioCrearBlog(request.POST)
        if formulario_crear_blog.is_valid():
            variable = models.Post()
            informacion = formulario_crear_blog.cleaned_data
            
            variable.titulo=informacion['titulo']
            variable.subtitulo=informacion['subtitulo']
            variable.contenido=informacion['contenido']
            variable.autor= request.user
            
            variable.save()
        return render(request,'Pages/posteos.html', {'posts' : posts, 'formulario_crear_blog': formulario_crear_blog})
    else:
        formulario_crear_blog = forms.FormularioCrearBlog()
        return render(request,'Pages/posteos.html', {'posts' : posts, 'formulario_crear_blog': formulario_crear_blog})

@login_required
def posteos_n(request,pk):
    post = Post.objects.filter(id=pk)[0]
    print (pk)
    print (post.id)
    return render(request, 'Pages/posteos_n.html', { 'post' : post })

class PostUpdateView(UpdateView):
    model = Post
    template_name = "Pages/post_update.html"
    fields = ["titulo", "subtitulo", "contenido"]
    success_url = reverse_lazy("Posteos")

class PostDeleteView(DeleteView):
    model = Post
    template_name = "Pages/post_delete.html"
    success_url = reverse_lazy("Posteos")

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from Appblog import forms, models

def inicio (request):
    return render(request,'Appblog/inicio.html')

def cursos(request):
    if request.method == 'POST':
        mi_formulario = forms.CursoFormulario(request.POST)
        
        print(mi_formulario)
        
        if mi_formulario.is_valid():
            
            informacion = mi_formulario.cleaned_data
            
            variable = models.Curso(nombre=informacion['nombre'], camada=informacion['camada'])
            
            variable.save()
        return redirect('Cursos')
    else:
        mi_formulario = forms.CursoFormulario()
        return render(request,'AppBlog/cursos.html', {'mi_formulario': mi_formulario})

def estudiantes (request):
    if request.method == 'POST':
        mi_formulario = forms.EstudianteFormulario(request.POST)

        if mi_formulario.is_valid():
            
            informacion = mi_formulario.cleaned_data
            
            variable = models.Estudiante(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            
            variable.save()
        return redirect('Estudiantes')
    else:
        mi_formulario = forms.EstudianteFormulario()
        return render(request,'AppBlog/estudiantes.html', {'mi_formulario': mi_formulario})

def profesores (request):
    if request.method == 'POST':
        mi_formulario = forms.ProfesorFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            variable = models.Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion'])  
            variable.save()
        return redirect('Profesores')
    else:
        mi_formulario = forms.ProfesorFormulario()
        return render(request,'AppBlog/profesores.html', {'mi_formulario': mi_formulario})

def entregables (request):
    if request.method == 'POST':
        mi_formulario = forms.EntregableFormulario(request.POST)
        if mi_formulario.is_valid():
            
            informacion = mi_formulario.cleaned_data
            
            variable = models.Entregable(nombre=informacion['nombre'], fecha_entrega=informacion['fecha_entrega'], entregado=informacion['entregado'])
            
            variable.save()
        return render(request,'AppBlog/entregables.html', {'mi_formulario': mi_formulario})
    else:
        mi_formulario = forms.EntregableFormulario()
        return render(request,'AppBlog/entregables.html', {'mi_formulario': mi_formulario})

def consultas (request):
    return render(request,'Appblog/consultas.html')

def consultas_cursos (request):
    variable = models.Curso.objects.all()
    return render(request,'Appblog/consultas_cursos.html',{"value" : variable})

def consultas_estudiantes (request):
    variable = models.Estudiante.objects.all()
    return render(request,'Appblog/consultas_estudiantes.html',{"value" : variable})

def consultas_profesores (request):
    variable = models.Profesor.objects.all()
    return render(request,'Appblog/consultas_profesores.html',{"value" : variable})

def consultas_entregables (request):
    try:
        entregables = models.Entregable.objects.filter(nombre=request.GET['entregable'])
        return render(request, "Appblog/resultado_busqueda.html", {"entregables": entregables, "nombre": request.GET['entregable']})
    except:
        return render(request,'Appblog/consultas_entregables.html')
    

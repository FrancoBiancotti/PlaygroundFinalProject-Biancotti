from django.urls import path
from Appblog import views

urlpatterns = [
    path('', views.inicio, name = 'Inicio'),
    path('cursos/', views.cursos, name = 'Cursos'),
    path('estudiantes/', views.estudiantes, name = 'Estudiantes'),
    path('profesores/', views.profesores, name = 'Profesores'),
    path('entregables/', views.entregables, name = 'Entregables'),
    path('consulta/', views.consultas, name = 'Consultas'),
    path('consulta_cursos/', views.consultas_cursos, name = 'ConsultaCursos'),
    path('consulta_estudiantes/', views.consultas_estudiantes, name = 'ConsultaEstudiantes'),
    path('consulta_profesores/', views.consultas_profesores, name = 'ConsultaProfesores'),
    path('consulta_entregables/', views.consultas_entregables, name = 'ConsultaEntregables'),
]
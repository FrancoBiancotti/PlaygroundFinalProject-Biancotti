from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from Appblog import forms, models

def inicio (request):
    return render(request,'About/inicio.html')
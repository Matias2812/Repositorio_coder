
from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Familia
from app_coder.models import Curso
from django.template import Context,loader
from django.http import HttpResponse
# Create your views here.

def curso(request):
    cursos = Curso.objects.all()
    dicc={'cursos': cursos}
    plantilla= loader.get_template('template.html')
    renderizar= plantilla.render(dicc)
    return HttpResponse(renderizar)


def alta_curso(request, nombre):
    curso = Curso(nombre = nombre, camada = '637490')
    curso.save()
    texto= f'Se guardo en la BD el Curso:: {curso.nombre} Camada: {curso.camada}'
    return HttpResponse(texto)


def info_familia(request):
    familia= Familia.objects.all()
    diccionario= {'nombre': familia}
    pantilla= loader.get_template('modelo.html')
    pantalla= pantilla.render(diccionario)
    return HttpResponse(pantalla)

def integrantes_familia(request, numero, fecha, cadena):
    familia= Familia(numero = numero, fecha = fecha, cadena = cadena)
    familia.save()
    oracion= f'Se guardo el Numero: {familia.numero}, Fecha: {familia.fecha} y Cadena, {familia.cadena}'
    return HttpResponse(oracion)
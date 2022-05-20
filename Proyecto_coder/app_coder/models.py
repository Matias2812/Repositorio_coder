from django.db import models

# Create your models here.


class Curso(models.Model):
    
    nombre= models.CharField(max_length=40)
    camada= models.IntegerField() 


class Familia(models.Model):
    
    numero = models.IntegerField()
    
    fecha = models.DateField()
    
    cadena = models.CharField(max_length=40)
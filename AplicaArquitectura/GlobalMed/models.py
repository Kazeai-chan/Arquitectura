from django.db import models
from django import forms

# Create your models here.
#clase pedidos
class reserva(models.Model):
    idreserva=models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=50) 
    correo=models.CharField(max_length=20) 
    fecha=models.DateField(verbose_name='Fecha')
    hora= models.CharField(max_length=30)
    departamento =models.IntegerField() 
    #departamento= models.CharField(max_length=30)
    doctor=models.IntegerField() 
    #doctor= models.CharField(max_length=30)
    comentario= models.CharField(max_length=50,blank=True)

    def __str__(self):
        return f'{self.nombre} {self.doctor}'
    
#lista docs
class doctores(models.Model):
    id=models.AutoField(primary_key=True) 
    nombre= models.CharField(max_length=50) 
    id_dep=models.IntegerField() 

    def __str__(self):
        return f'{self.nombre}'
#fin de la clase

#lista depart
class departamentos(models.Model):
    id=models.AutoField(primary_key=True) 
    nombre_dep= models.CharField(max_length=30) 

    def __str__(self):
        return f'{self.nombre_dep}'
#fin de la clase
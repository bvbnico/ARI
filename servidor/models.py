from __future__ import unicode_literals
from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid # Requerida para ids unicos
from datetime import datetime
from django.contrib.auth.models import AbstractUser
#from fcm_django.models import FCMDevice
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class estaciones(models.Model):
    #modelo que representa las estaciones de bombero
    estacion_id = models.PositiveIntegerField()
    nombre = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    latitud = models.CharField(max_length=20)
    longitud = models.CharField(max_length=20)
    nro_telefonico = models.CharField(max_length=20)
    def __unicode__(self):
        return '%d %s %s %s %s %s' % (self.estacion_id, self.nombre, self.direccion, self.latitud,
        self.longitud,self. nro_telefonico)
    def __str__(self):
        return '%d %s %s %s %s %s %s' % (self.estacion_id, self.ciudad, self.nombre, self.direccion, self.latitud,
        self.longitud,self.nro_telefonico)


class clientes(models.Model):
    #representa los clientes con todos sus datos
    estacion = models.ForeignKey(estaciones, on_delete=models.SET_NULL, null=True)
    cliente_id = models.PositiveIntegerField()
    LOAN_STATUS = (
        ('p', 'Particular'),
        ('e', 'Empresa'),
    )
    tipo = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='p', help_text='Tipo de cliente')
    descripcion = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    ci_nro = models.CharField(max_length=20)
    ruc = models.CharField(max_length=20)
    nro_telefonico = models.CharField(max_length=20)
    contacto = models.CharField(max_length=200)
    nro_celular = models.CharField(max_length=20)
    latitud = models.CharField(max_length=20)
    longitud = models.CharField(max_length=20)
    referencias = models.CharField(max_length=200)
    #plano:
    obs = models.CharField(max_length=200)
    nro_sensores = models.PositiveIntegerField()
    def __unicode__(self):
           return '%s %d %s %s %s %s %s %s %s %s %s %s %s %s %s %d' % (self.estaciones, self.cliente_id, self.tipo, self. descripcion,
           self.nombre,self.apellido,self.ci_nro,self.ruc,self.nro_telefonico,self.contacto,self.nro_celular,
           self.latitud,self.longitud,self.referencias,self.plano,self.obs,self.nro_sensores)
    def __str__(self):
           return '%d %s %s %s %s %s %s %s %s %s %s %s %s %s %d' % (self.cliente_id, self.tipo, self. descripcion,
           self.nombre,self.apellido,self.ci_nro,self.ruc,self.nro_telefonico,self.contacto,self.nro_celular,
           self.latitud,self.longitud,self.referencias,self.obs,self.nro_sensores)


class sensores(models.Model):
    #representa los datos de todos los nro_sensores
    cliente = models.ForeignKey(clientes, on_delete=models.SET_NULL, null=True)
    sensor_id: models.PositiveIntegerField()
    tipo = models. ForeignKey('tipo_sensor', on_delete=models.SET_NULL, null=True)
    sector = models.CharField(max_length=1)
    def __unicode__(self):
        return '%s %d %s %s' % (self.cliente, self.sensor_id, self.tipo, self.sector)

class tipo_sensor(models.Model):
    #representa los tipos de sensores existentes
    tipo = models.CharField(max_length=200)
    def __str__(self):
        return self.tipo


class usuarios(models.Model):
    #representa los usuarios y niveles
    cargo= (
    ('Sp', 'Supervisor'),
    ('En', 'Encargado de turno'),
)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    puesto = models.CharField(max_length=15,choices=cargo)
    estacion = models.ForeignKey(estaciones, on_delete=models.SET_NULL, null=True)
    def __unicode__(self):
            return '%s %s %s %s' % (self.nombre, self.apellido, self.puesto, self.estacion)

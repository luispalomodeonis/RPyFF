#------------------------------------------------------
#  Sección de importación de módulos
#------------------------------------------------------
from django.db import models
from django.conf import settings
from django.urls import reverse
from datetime import date
import datetime
import uuid


#------------------------------------------------------
#  Modelo de Letra
#     Solo admite letras del castellano estándar
#     No existen refranes con la letra Ñ
#     Son aprobadas en su directamente en su creación
#------------------------------------------------------
class Letra(models.Model):
   id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        #help_text="Introduce un identificador numérico"
        )
   letra = models.CharField(
           'Letra',
           max_length=1,
           unique=True,
           #help_text="Introduce una letra"
           )

   class Meta:
      ordering = ['letra']

   def get_absolute_url(self):
      return reverse ('letra-detalle', args=[str(self.id)])

   def __str__(self):
      return f'{self.letra}'

#------------------------------------------------------
#  Modelo de Origen
#     Se conserva fecha de alta
#     Mantiene estados Revisión y Aprobado
#------------------------------------------------------
class Origen(models.Model):
   id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        #help_text="Introduce un identificador numérico"
        )
   nombre = models.CharField(
            'Nombre',
            max_length=120,
            #help_text="Introduce un nombre"
            )
   fecha = models.DateField(
           'Registrado',
           null=True,
           blank=True
           )
   ESTADOS = (
         ('r', 'Revisión'),
         ('a', 'Aprobado'),
      )
   estado = models.CharField(
            'Estado',
            max_length=1,
            choices=ESTADOS,
            blank=True,
            default='r',
            #help_text="Selecciona un estado"
            )

   class Meta:
      ordering = ['nombre']

   def get_absolute_url(self):
      return reverse('origen-detalle', args=[str(self.id)])

   def __str__(self):
      return  f'{self.nombre}'

   @property
   def no_aprobado(self):
      return bool(self.estado != 'a')

   def get_palabras(self):
      return self.palabra_set.all



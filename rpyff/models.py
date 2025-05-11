
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
#     Son aprobadas en su creación
#------------------------------------------------------
class Letra(models.Model):
   id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        )
   letra = models.CharField(
           'Letra',
           max_length=1,
           unique=True,
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
        )
   nombre = models.CharField(
            'Nombre',
            max_length=120,
            help_text="Introduce un nombre de Origen"
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

#------------------------------------------------------
#  Modelo de Palabra
#     Se conserva fecha de alta
#     Mantiene estados Revisión y Aprobada
#     Tiene tres relaciones 1 a N con claves foráneas
#        con entidades Letra, Origen y usuario autenticado
#     Es antigua si fué creada un año antes de la fecha actual
#        (no se emplea en la aplicación)
#------------------------------------------------------
class Palabra(models.Model):
   id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        )
   palabra = models.CharField(
             'Palabra',
             max_length=51,
             help_text="Introduce una palabra"
             )
   significado = models.TextField(
             'Significado',
             max_length=512,
             default="",
             help_text="Introduce el significado de la palabra"
             )
   fecha = models.DateField(
           'Registrada',
           default=date.today,
           null=True,
           blank=True
           )
   letra = models.ForeignKey(
           'Letra',
           on_delete=models.RESTRICT,
           null=False
           )

   origen = models.ForeignKey(
            'Origen',
            on_delete=models.RESTRICT,
            null=True
            )
   creador = models.ForeignKey(
             settings.AUTH_USER_MODEL,
             on_delete=models.SET_NULL,
             null=True,
             blank=True
             )
   ESTADOS = (
         ('r', 'Revisión'),
         ('a', 'Aprobada'),
      )
   estado = models.CharField(
            'Estado',
            max_length=1,
            choices=ESTADOS,
            blank=True,
            default='r',
            )

   @property
   def es_antigua(self):
      return bool(self.fecha and self.creador and self.fecha < date.today() - datetime.timedelta(weeks=52))

   @property
   def en_revision(self):
      return bool(self.estado == 'r')

   @property
   def no_aprobada(self):
      return bool(self.estado != 'a')

   class Meta:
       ordering = ['palabra','letra','origen','fecha']

   def get_absolute_url(self):
      return reverse ('palabra-detalle', args=[str(self.id)])

   def __str__(self):
      return f'{self.palabra}'

#------------------------------------------------------
#  Modelo de Refran
#     Se conserva fecha de alta, de aprobación y publicación
#     Mantiene estados Revisión, Aprobado y Publicado
#     Tiene cuatro relaciones 1 a N con claves foráneas
#        con entidades Letra, Origen, Palabra  y usuario autenticado
#     Tiene 1 relación N-M con otras palabras
#     Es antiguo si fué creada un año antes de la fecha actual
#        (no se emplea en la aplicación)
#        (debería considerarse si lleva mucho tiempo
#            sin aprobar o publicar desde su creación
#------------------------------------------------------
class Refran(models.Model):
   id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        )
   dicho = models.TextField(
           'Refrán',
           max_length=191,
           help_text="Introduce el refrán"
           )
   explicacion = models.TextField(
                 'Explicación',
                 max_length=512,
                 help_text="Introduce una explicación para el refrán"
                 )
   fecha = models.DateField(
           'Registrado',
           default=date.today,
           null=True,
           blank=True
           )
   fechaaprobacion = models.DateField(
           'Aprobado',
           null=True,
           blank=True
           )
   fechapublicacion = models.DateField(
           'Publicado',
           null=True,
           blank=True
           )
   ESTADOS = (
         ('r', 'Revisión'),
         ('a', 'Aprobado'),
         ('p', 'Publicado')
      )
   estado = models.CharField(
            'Estado',
            max_length=1,
            choices=ESTADOS,
            blank=True,
            default='r',
            )
   letra = models.ForeignKey(
           'Letra',
           on_delete=models.RESTRICT,
           null=False
           )
   palabra = models.ForeignKey(
             'Palabra',
             on_delete=models.RESTRICT,
             null=True,
             related_name='palabra_base_refran'
             )
   otraspalabras = models.ManyToManyField(
             'Palabra',
#             on_delete=models.RESTRICT,
#             null=True
             )
   origen = models.ForeignKey(
            'Origen',
            on_delete=models.RESTRICT,
            null=True
            )
   creador = models.ForeignKey(
             settings.AUTH_USER_MODEL,
             on_delete=models.SET_NULL,
             null=True,
             blank=True
             )
   class Meta:
#      ordering = ['palabras', 'fecha', 'fechaaprobacion', 'fechapublicacion']
      ordering = ['palabra', 'fecha', 'fechaaprobacion', 'fechapublicacion']

   @property
   def es_antiguo(self):
      return bool(self.fecha and self.creador and self.fecha < date.today() - datetime.timedelta(weeks=52))

   @property
   def no_publicado(self):
      return bool(self.estado != 'p')

   def get_absolute_url(self):
      return reverse ('refran-detalle', args=[str(self.id)])

   def __str__(self):
      return f'{self.dicho}'

   @property
   def get_context_data(self, **kwargs):
      context=get_context_data(**kwargs)
      context["nombre_estado"]=get_estado_display()
      return context
#------------------------------------------------------
#  Modelo de Proverbio
#     Se conserva fecha de alta, de aprobación y publicación
#     Mantiene estados Revisión, Aprobado y Publicado
#     Tiene cuatro relaciones 1 a N con claves foráneas
#        con entidades Letra, Origen, Palabra  y usuario autenticado
#     Tiene 1 relación N-M con otras palabras
#     Es antiguo si fué creada un año antes de la fecha actual
#        (no se emplea en la aplicación)
#        (debería considerarse si lleva mucho tiempo
#            sin aprobar o publicar desde su creación
#------------------------------------------------------
class Proverbio(models.Model):
   id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        )
   dicho = models.TextField(
           'Proverbio',
           max_length=191,
           help_text="Introduce el proverbio"
           )
   explicacion = models.TextField(
                 'Explicación',
                 max_length=512,
                 help_text="Introduce una explicación para el proverbio"
                 )
   fecha = models.DateField(
           'Registrado',
           default=date.today,
           null=True,
           blank=True
           )
   fechaaprobacion = models.DateField(
           'Aprobado',
           null=True,
           blank=True
           )
   fechapublicacion = models.DateField(
           'Publicado',
           null=True,
           blank=True
           )
   ESTADOS = (
         ('r', 'Revisión'),
         ('a', 'Aprobado'),
         ('p', 'Publicado')
      )
   estado = models.CharField(
            'Estado',
            max_length=1,
            choices=ESTADOS,
            blank=True,
            default='r',
            )
   letra = models.ForeignKey(
           'Letra',
           on_delete=models.RESTRICT,
           null=False
           )
   palabra = models.ForeignKey(
             'Palabra',
             on_delete=models.RESTRICT,
             null=True,
             related_name='palabra_base_proverbio'
             )
   otraspalabras = models.ManyToManyField(
             'Palabra',
#             on_delete=models.RESTRICT,
#             null=True
             )
   origen = models.ForeignKey(
            'Origen',
            on_delete=models.RESTRICT,
            null=True
            )
   creador = models.ForeignKey(
             settings.AUTH_USER_MODEL,
             on_delete=models.SET_NULL,
             null=True,
             blank=True
             )
   class Meta:
#      ordering = ['palabras', 'fecha', 'fechaaprobacion', 'fechapublicacion']
      ordering = ['palabra', 'fecha', 'fechaaprobacion', 'fechapublicacion']

   @property
   def es_antiguo(self):
      return bool(self.fecha and self.creador and self.fecha < date.today() - datetime.timedelta(weeks=52))

   @property
   def no_publicado(self):
      return bool(self.estado != 'p')

   def get_absolute_url(self):
      return reverse ('proverbio-detalle', args=[str(self.id)])

   def __str__(self):
      return f'{self.dicho}'

   @property
   def get_context_data(self, **kwargs):
      context=get_context_data(**kwargs)
      context["nombre_estado"]=get_estado_display()
      return context
#------------------------------------------------------
#  Modelo de Frase
#     Se conserva fecha de alta, de aprobación y publicación
#     Mantiene estados Revisión, Aprobado y Publicado
#     Tiene cuatro relaciones 1 a N con claves foráneas
#        con entidades Letra, Origen, Palabra  y usuario autenticado
#     Tiene 1 relación N-M con otras palabras
#     Es antiguo si fué creada un año antes de la fecha actual
#        (no se emplea en la aplicación)
#        (debería considerarse si lleva mucho tiempo
#            sin aprobar o publicar desde su creación
#------------------------------------------------------
class Frase(models.Model):
   id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        )
   dicho = models.TextField(
           'Frase',
           max_length=191,
           help_text="Introduce la frase"
           )
   explicacion = models.TextField(
                 'Explicación',
                 max_length=512,
                 help_text="Introduce una explicación o autor"
                 )
   fecha = models.DateField(
           'Registrado',
           default=date.today,
           null=True,
           blank=True
           )
   fechaaprobacion = models.DateField(
           'Aprobado',
           null=True,
           blank=True
           )
   fechapublicacion = models.DateField(
           'Publicado',
           null=True,
           blank=True
           )
   ESTADOS = (
         ('r', 'Revisión'),
         ('a', 'Aprobado'),
         ('p', 'Publicado')
      )
   estado = models.CharField(
            'Estado',
            max_length=1,
            choices=ESTADOS,
            blank=True,
            default='r',
            )
   letra = models.ForeignKey(
           'Letra',
           on_delete=models.RESTRICT,
           null=False
           )
   palabra = models.ForeignKey(
             'Palabra',
             on_delete=models.RESTRICT,
             null=True,
             related_name='palabra_base_frase'
             )
   otraspalabras = models.ManyToManyField(
             'Palabra',
#             on_delete=models.RESTRICT,
              #null=True,
              blank=True
             )
   origen = models.ForeignKey(
            'Origen',
            on_delete=models.RESTRICT,
            null=True
            )
   creador = models.ForeignKey(
             settings.AUTH_USER_MODEL,
             on_delete=models.SET_NULL,
             null=True,
             blank=True
             )
   class Meta:
#      ordering = ['palabras', 'fecha', 'fechaaprobacion', 'fechapublicacion']
      ordering = ['palabra', 'fecha', 'fechaaprobacion', 'fechapublicacion']

   @property
   def es_antiguo(self):
      return bool(self.fecha and self.creador and self.fecha < date.today() - datetime.timedelta(weeks=52))

   @property
   def no_publicado(self):
      return bool(self.estado != 'p')

   def get_absolute_url(self):
      return reverse ('frase-detalle', args=[str(self.id)])

   def __str__(self):
      return f'{self.dicho}'

   @property
   def get_context_data(self, **kwargs):
      context=get_context_data(**kwargs)
      context["nombre_estado"]=get_estado_display()
      return context
#----------------------------------------------------
#   Fin de los modelos de datos
#----------------------------------------------------

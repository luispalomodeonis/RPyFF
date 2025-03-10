
from django.contrib.auth.mixins import PermissionRequiredMixin
from django import forms
from django.db import models

from .models import Palabra, Refran, Proverbio, Frase

class PalabraForm(forms.ModelForm):

   class Meta:
      model=Palabra
      fields=('palabra', 'significado','letra','origen','estado')
      permission_required='refran.add_palabra'

class RefranForm(forms.ModelForm):

   class Meta:
      model=Refran
      fields=('dicho', 'explicacion','letra','palabra','otraspalabras','origen','estado')
      permission_required='refran.add_refran'

class ProverbioForm(forms.ModelForm):

   class Meta:
      model=Proverbio
      fields=('dicho', 'explicacion','letra','palabra','otraspalabras','origen','estado')
      permission_required='refran.add_proverbio'

class FraseForm(forms.ModelForm):

   class Meta:
      model=Frase
      fields=('dicho', 'explicacion','letra','palabra','otraspalabras','origen','estado')
      permission_required='refran.add_frase'
   #otraspalabras = forms.ModelMultipleChoiceField(
   #   queryset=Palabra.objects.all(),
   #   widget=forms.CheckboxSelectMultiple
   #)
class BusquedaForm(forms.Form):
   mibusqueda=forms.CharField(label='Búsqueda global', max_length=33, required=False)
   mibusqueda_palabra=forms.CharField(label='Búsqueda por palabra', max_length=33, required=False)
   mibusqueda_significado=forms.CharField(label='Búsqueda por significado', max_length=33, required=False)
   mibusqueda_dicho=forms.CharField(label='Búsqueda por dicho', max_length=33, required=False)
   mibusqueda_explicacion=forms.CharField(label='Búsqueda por explicación', max_length=33, required=False)
   mibusqueda_numero=forms.IntegerField(label='Búsqueda por número', required=False)

   class Meta:
      fields=('mibusqueda','mibusqueda_palabra', 'mibusqueda_significado', 'mibusqueda_dicho', 'mibusqueda_explicacion', 'mibusqueda_numero')

class ContactForm(forms.Form):
   asunto = forms.CharField(max_length=100)
   mensaje = forms.CharField(widget=forms.Textarea)
   remitente = forms.EmailField()
   concopia = forms.BooleanField(label='Recibir copia',required=False)



#------------------------------------------------------
#  Sección de importación de módulos
#------------------------------------------------------

import random
import datetime
from datetime import datetime
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.views.generic.list import MultipleObjectMixin
from django.db.models import Q

from .models import Letra, Origen, Palabra, Refran, Proverbio, Frase
from .forms import PalabraForm
from .forms import RefranForm
from .forms import ProverbioForm
from .forms import FraseForm
from .forms import BusquedaForm
from .forms import ContactForm

# Importamos las clases creadas en el archivo views_pdf
#from . import views_pdf

#------------------------------------------------------
#  Vista de Contacto
#------------------------------------------------------
def contacto(request):
   if request.method=="POST":
      form=ContactForm(request.POST)
      if form.is_valid():
         asunto = form.cleaned_data["asunto"]
         mensaje = form.cleaned_data["mensaje"]
         remitente = form.cleaned_data["remitente"]
         concopia = form.cleaned_data["concopia"]
         #recipients = ["lpdeonis@gmail.com"]
         recipients = []

         if concopia:
            recipients.append(remitente)

         #send_mail(asunto, mensaje, remitente, recipients)
         send_mail(asunto, mensaje, remitente, recipients, fail_silently=False)
         #gracias_url = reverse_lazy('gracias', kwargs={"remitente":remitente})
         gracias_url = reverse_lazy('gracias')
         return redirect(gracias_url)
   else:
      form=ContactForm()
   return render(request, 'rpyff/contacto_form.html', {'form':form})

#def Gracias(request, **kwargs):
   #remitente=kwargs['remitente']
   #sender=request.POST.get('sender', None)
   #context = {
   #   'remitente': remitente
   #   }
   #return render(request, 'refran/gracias.html', context=context)
def Gracias(request):
   return render(request, 'rpyff/gracias.html')

#------------------------------------------------------
#  Vistas de Búsqueda
#------------------------------------------------------
def buscar(request):
   if request.method=="POST":
      form=BusquedaForm(request.POST)
      if form.is_valid():
         mibusqueda=request.POST.get('mibusqueda', None)
         mibusqueda_palabra=request.POST.get('mibusqueda_palabra', None)
         mibusqueda_significado=request.POST.get('mibusqueda_significado', None)
         mibusqueda_refran=request.POST.get('mibusqueda_refran', None)
         mibusqueda_explicacion=request.POST.get('mibusqueda_explicacion', None)
         success_url = reverse_lazy('refran-buscado', kwargs={"mibusqueda":mibusqueda,
            "mibusqueda_palabra":mibusqueda_palabra,
            "mibusqueda_significado":mibusqueda_significado,
            "mibusqueda_refran":mibusqueda_refran,
            "mibusqueda_explicacion":mibusqueda_explicacion
            })
         return redirect(success_url)
   else:
      form=BusquedaForm()
   return render(request, 'rpyff/busca_form.html', {'form':form})

def buscar_palabra(request):
   if request.method=="POST":
      form=BusquedaForm(request.POST)
      if form.is_valid():
         mibusqueda_palabra=request.POST.get('mibusqueda_palabra', None)
         success_url = reverse_lazy('palabra-buscada', kwargs={
            "mibusqueda_palabra":mibusqueda_palabra
            })
         return redirect(success_url)
   else:
      form=BusquedaForm()
   return render(request, 'rpyff/busca_form.html', {'form':form})

def buscar_significado(request):
   if request.method=="POST":
      form=BusquedaForm(request.POST)
      if form.is_valid():
         mibusqueda_significado=request.POST.get('mibusqueda_significado', None)
         success_url = reverse_lazy('significado-buscado', kwargs={
            "mibusqueda_significado":mibusqueda_significado
            })
         return redirect(success_url)
   else:
      form=BusquedaForm()
   return render(request, 'rpyff/busca_form.html', {'form':form})

def buscar_refran(request):
   if request.method=="POST":
      form=BusquedaForm(request.POST)
      if form.is_valid():
         mibusqueda_refran=request.POST.get('mibusqueda_refran', None)
         success_url = reverse_lazy('refran-buscado', kwargs={
            "mibusqueda_refran":mibusqueda_refran
            })
         return redirect(success_url)
   else:
      form=BusquedaForm()
   return render(request, 'rpyff/busca_form.html', {'form':form})

def buscar_proverbio(request):
   if request.method=="POST":
      form=BusquedaForm(request.POST)
      if form.is_valid():
         mibusqueda_proverbio=request.POST.get('mibusqueda_proverbio', None)
         success_url = reverse_lazy('proverbio-buscado', kwargs={
            "mibusqueda_proverbio":mibusqueda_proverbio
            })
         return redirect(success_url)
   else:
      form=BusquedaForm()
   return render(request, 'rpyff/busca_form.html', {'form':form})

def buscar_frase(request):
   if request.method=="POST":
      form=BusquedaForm(request.POST)
      if form.is_valid():
         mibusqueda_frase=request.POST.get('mibusqueda_frase', None)
         success_url = reverse_lazy('frase-buscada', kwargs={
            "mibusqueda_frase":mibusqueda_frase
            })
         return redirect(success_url)
   else:
      form=BusquedaForm()
   return render(request, 'rpyff/busca_form.html', {'form':form})

def buscar_explicacion(request):
   if request.method=="POST":
      form=BusquedaForm(request.POST)
      if form.is_valid():
         mibusqueda_explicacion=request.POST.get('mibusqueda_explicacion', None)
         success_url = reverse_lazy('explicacion-buscada', kwargs={
            "mibusqueda_explicacion":mibusqueda_explicacion
            })
         return redirect(success_url)
   else:
      form=BusquedaForm()
   return render(request, 'rpyff/busca_form.html', {'form':form})

def buscar_numero(request):
   if request.method=="POST":
      form=BusquedaForm(request.POST)
      if form.is_valid():
         mibusqueda_numero=request.POST.get('mibusqueda_numero', None)
         success_url = reverse_lazy('numero-buscado', kwargs={
            "mibusqueda_numero":mibusqueda_numero
            })
         return redirect(success_url)
   else:
      form=BusquedaForm()
   return render(request, 'rpyff/busca_form.html', {'form':form})

#----------------------------------------------------------
#    Vistas de Busquedas
#----------------------------------------------------------
class PalabraBuscada(generic.ListView, MultipleObjectMixin):
   template_name = 'rpyff/buscada_palabra.html'
   paginate_by = 10
   
   def get_queryset(self,**kwargs):
       self.mibusqueda_palabra=self.kwargs['mibusqueda_palabra']
# ??? esto hay que evitarlo
       return Refran.objects.filter(estado__exact='x')

   def get_context_data(self, **kwargs):
      object_list = Palabra.objects.filter(palabra__icontains=self.mibusqueda_palabra).filter(estado__exact='a')
      context = super(PalabraBuscada,self).get_context_data(object_list=object_list, **kwargs)
      mibusqueda_palabra=self.kwargs['mibusqueda_palabra']
      if mibusqueda_palabra != None:
         context['mibusqueda_palabra']=self.mibusqueda_palabra
      return context

class SignificadoBuscado(generic.ListView, MultipleObjectMixin):
   template_name = 'rpyff/buscado_significado.html'
   paginate_by = 10
   
   def get_queryset(self,**kwargs):
       self.mibusqueda_significado=self.kwargs['mibusqueda_significado']
# ??? esto hay que evitarlo
       return Refran.objects.filter(estado__exact='x')

   def get_context_data(self, **kwargs):
      object_list = Palabra.objects.filter(significado__icontains=self.mibusqueda_significado).filter(estado__exact='a')
      context = super(SignificadoBuscado,self).get_context_data(object_list=object_list, **kwargs)
      mibusqueda_significado=self.kwargs['mibusqueda_significado']
      if mibusqueda_significado != None:
         context['mibusqueda_significado']=self.mibusqueda_significado
      return context

class RefranBuscado(generic.ListView, MultipleObjectMixin):
   template_name = 'rpyff/buscado_refran.html'
   paginate_by = 10
   
   def get_queryset(self,**kwargs):
       self.mibusqueda_refran=self.kwargs['mibusqueda_refran']
# ??? esto hay que evitarlo
       return Refran.objects.filter(estado__exact='x')

   def get_context_data(self, **kwargs):
      object_list = Refran.objects.filter(dicho__icontains=self.mibusqueda_refran).filter(~Q(estado='r'))
      context = super(RefranBuscado,self).get_context_data(object_list=object_list,**kwargs)
      mibusqueda_refran=self.kwargs['mibusqueda_refran']
      if mibusqueda_refran != None:
         context['mibusqueda_refran']=self.mibusqueda_refran
      return context

class ProverbioBuscado(generic.ListView, MultipleObjectMixin):
   template_name = 'rpyff/buscado_proverbio.html'
   paginate_by = 10
   
   def get_queryset(self,**kwargs):
       self.mibusqueda_proverbio=self.kwargs['mibusqueda_proverbio']
# ??? esto hay que evitarlo
       return Proverbio.objects.filter(estado__exact='x')

   def get_context_data(self, **kwargs):
      object_list = Proverbio.objects.filter(dicho__icontains=self.mibusqueda_proverbio).filter(~Q(estado='r'))
      context = super(ProverbioBuscado,self).get_context_data(object_list=object_list,**kwargs)
      mibusqueda_proverbio=self.kwargs['mibusqueda_proverbio']
      if mibusqueda_proverbio != None:
         context['mibusqueda_proverbio']=self.mibusqueda_proverbio
      return context

class FraseBuscada(generic.ListView, MultipleObjectMixin):
   template_name = 'rpyff/buscada_frase.html'
   paginate_by = 10
   
   def get_queryset(self,**kwargs):
       self.mibusqueda_frase=self.kwargs['mibusqueda_frase']
# ??? esto hay que evitarlo
       return Frase.objects.filter(estado__exact='x')

   def get_context_data(self, **kwargs):
      object_list = Frase.objects.filter(dicho__icontains=self.mibusqueda_frase).filter(~Q(estado='r'))
      context = super(FraseBuscada,self).get_context_data(object_list=object_list,**kwargs)
      mibusqueda_frase=self.kwargs['mibusqueda_frase']
      if mibusqueda_frase != None:
         context['mibusqueda_frase']=self.mibusqueda_frase
      return context

class ExplicacionBuscada(generic.ListView, MultipleObjectMixin):
   template_name = 'rpyff/buscada_explicacion.html'
   paginate_by = 5
   
   def get_queryset(self,**kwargs):
       self.mibusqueda_explicacion=self.kwargs['mibusqueda_explicacion']
# ??? esto hay que evitarlo
       return Refran.objects.filter(estado__exact='x')

   def get_context_data(self, **kwargs):
      object_list_ref =Refran.objects.filter(explicacion__icontains=self.mibusqueda_explicacion).filter(~Q(estado='r')).annotate(tipo=Value('r'))
      object_list_pro =Proverbio.objects.filter(explicacion__icontains=self.mibusqueda_explicacion).filter(~Q(estado='r')).annotate(tipo=Value('p'))
      object_list_fra =Frase.objects.filter(explicacion__icontains=self.mibusqueda_explicacion).filter(~Q(estado='r')).annotate(tipo=Value('f'))
      object_list_1=[]
      if object_list_ref and object_list_pro:
         object_list_1 = list(chain(object_list_ref,object_list_pro))
      elif object_list_ref:
         object_list_1 = object_list_ref
      elif object_list_pro:
         object_list_1 = object_list_pro
      if object_list_1 and object_list_fra:
         object_list_1 = list(chain(object_list_1,object_list_fra))
      elif object_list_fra:
         object_list_1 = object_list_fra
      #else:
      #   object_list_1 = object_list_ref
      object_list = object_list_1
      context = super(ExplicacionBuscada,self).get_context_data(object_list=object_list, **kwargs)
      mibusqueda_explicacion=self.kwargs['mibusqueda_explicacion']
      if mibusqueda_explicacion != None:
         context['mibusqueda_explicacion']=self.mibusqueda_explicacion
      return context

class NumeroBuscado(generic.ListView, MultipleObjectMixin):
   template_name = 'rpyff/buscado_numero.html'
   paginate_by = 10
   
   def get_queryset(self,**kwargs):
       self.mibusqueda_numero=self.kwargs['mibusqueda_numero']
# ??? esto hay que evitarlo
       return Refran.objects.filter(estado__exact='x')

   def get_context_data(self, **kwargs):
      num_refranes_aprobados = Refran.objects.filter(~Q(estado='r')).count()
      mibusqueda_numero=self.kwargs['mibusqueda_numero']
      if num_refranes_aprobados >= int(mibusqueda_numero) and mibusqueda_numero != None:
         #object_list = Refran.objects.filter(~Q(estado='r')).order_by('fecha').order_by('fechaaprobacion').order_by('fechapublicacion')[int(self.mibusqueda_numero)-1]
         object_list = Refran.objects.filter(~Q(estado='r')).order_by('fecha').order_by('fechaaprobacion')[int(self.mibusqueda_numero)-1]
         context={
            'object_list':object_list
         }
         context['mibusqueda_numero']=self.mibusqueda_numero
      else:
         context={}
      return context

import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

#------------------------------------------------------
#  Vista de función de index
#------------------------------------------------------
def index(request):
   num_refranes = Refran.objects.all().count()
   num_refranes_revision = Refran.objects.filter(estado__exact='r').count()
   num_refranes_aprobados = Refran.objects.filter(~Q(estado='r')).count()
   #num_refranes_publicados = Refran.objects.filter(estado__exact='p').count()
   num_proverbios = Proverbio.objects.all().count()
   num_proverbios_revision = Proverbio.objects.filter(estado__exact='r').count()
   num_proverbios_aprobados = Proverbio.objects.filter(~Q(estado='r')).count()
   #num_proverbios_publicados = Proverbio.objects.filter(estado__exact='p').count()
   num_frases = Frase.objects.all().count()
   num_frases_revision = Frase.objects.filter(estado__exact='r').count()
   num_frases_aprobadas = Frase.objects.filter(~Q(estado='r')).count()
   #num_frases_publicadas = Frase.objects.filter(estado__exact='p').count()
   #num_visitas = request.session.get('num_visitas', 0)
   fecha=datetime.now().today()
   dt = datetime.now()
   fecha_ano = dt.year
   fecha_mes = dt.month
   fecha_dia = dt.day
   fecha='%s%s%s' % (fecha_ano,fecha_mes,fecha_dia)
   resto = 0
   if (num_refranes_aprobados !=0):
      resto=str((int(fecha)*19)%int(num_refranes_aprobados+num_proverbios_aprobados+num_frases_aprobadas))
      num_aleatorio_r=random.randint(1, num_refranes_aprobados)
      refran_aleatorio=Refran.objects.filter(~Q(estado='r')).order_by('fecha').order_by('fechaaprobacion').order_by('fechapublicacion')[num_aleatorio_r-1]
      refran_aleatorio_id=refran_aleatorio.id
      refran_dicho=refran_aleatorio.dicho
      refran_explicacion=refran_aleatorio.explicacion
      refran_palabra=refran_aleatorio.palabra.palabra
      refran_palabra_id=refran_aleatorio.palabra.id
   else:
      refran_palabra=""
      refran_palabra_id=""
      refran_dicho=""
      refran_explicacion=""
      num_aleatorio_r=0
      refran_aleatorio_id=""
   if (num_proverbios_aprobados !=0):
      num_aleatorio_p=random.randint(1, num_proverbios_aprobados)
      proverbio_aleatorio=Proverbio.objects.filter(~Q(estado='r')).order_by('fecha').order_by('fechaaprobacion').order_by('fechapublicacion')[num_aleatorio_p-1]
      proverbio_aleatorio_id=proverbio_aleatorio.id
      proverbio_dicho=proverbio_aleatorio.dicho
      proverbio_explicacion=proverbio_aleatorio.explicacion
      proverbio_palabra=proverbio_aleatorio.palabra.palabra
      proverbio_palabra_id=proverbio_aleatorio.palabra.id
   else:
      proverbio_palabra=""
      proverbio_palabra_id=""
      proverbio_dicho=""
      proverbio_explicacion=""
      num_aleatorio_p=0
      proverbio_aleatorio_id=""
   if (num_frases_aprobadas !=0):
      num_aleatorio_f=random.randint(1, num_frases_aprobadas)
      frase_aleatorio=Frase.objects.filter(~Q(estado='r')).order_by('fecha').order_by('fechaaprobacion').order_by('fechapublicacion')[num_aleatorio_f-1]
      frase_aleatorio_id=frase_aleatorio.id
      frase_dicho=frase_aleatorio.dicho
      frase_explicacion=frase_aleatorio.explicacion
      frase_palabra=frase_aleatorio.palabra.palabra
      frase_palabra_id=frase_aleatorio.palabra.id
   else:
      frase_palabra=""
      frase_palabra_id=""
      frase_dicho=""
      frase_explicacion=""
      num_aleatorio_f=0
      frase_aleatorio_id=""
      #cita_deldia=""
   if (int(resto)<=num_refranes_aprobados):
      #print("Resto:",resto)
      #cita_deldia=Refran.objects.filter(~Q(estado='r')).order_by('fecha').order_by('fechaaprobacion').order_by('fechapublicacion').annotate(tipo=Value('r'))[int(resto)-1]
      cita_deldia=Refran.objects.filter(~Q(estado='r')).order_by('fecha').order_by('fechaaprobacion').order_by('fechapublicacion').annotate(tipo=Value('r'))[int(resto)]
   elif (int(resto)<=num_proverbios_aprobados+num_refranes_aprobados):
      cita_deldia=Proverbio.objects.filter(~Q(estado='r')).order_by('fecha').order_by('fechaaprobacion').order_by('fechapublicacion').annotate(tipo=Value('p'))[int(resto)-int(num_refranes_aprobados)-1]
   else:
      cita_deldia=Proverbio.objects.filter(~Q(estado='r')).order_by('fecha').order_by('fechaaprobacion').order_by('fechapublicacion').annotate(tipo=Value('f'))[int(resto)-int(num_refranes_aprobados)-int(num_proverbios_aprobados)-1]
   context = {
      'num_refranes':num_refranes,
      'num_refranes_revision': num_refranes_revision,
      'num_refranes_aprobados': num_refranes_aprobados,
      #'num_refranes_publicados': num_refranes_publicados,
      'num_proverbios':num_proverbios,
      'num_proverbios_revision': num_proverbios_revision,
      'num_proverbios_aprobados': num_proverbios_aprobados,
      #'num_proverbios_publicados': num_proverbios_publicados,
      'num_frases':num_frases,
      'num_frases_revision': num_frases_revision,
      'num_frases_aprobadas': num_frases_aprobadas,
      #'num_frases_publicadas': num_frases_publicadas,
      'refran_aleatorio':refran_aleatorio_id,
      'refran_numero':num_aleatorio_r,
      'refran_dicho':refran_dicho,
      'refran_palabra':refran_palabra,
      'refran_palabra_id':refran_palabra_id,
      'refran_explicacion':refran_explicacion,
      'proverbio_aleatorio':proverbio_aleatorio_id,
      'proverbio_numero':num_aleatorio_p,
      'proverbio_dicho':proverbio_dicho,
      'proverbio_palabra':proverbio_palabra,
      'proverbio_palabra_id':proverbio_palabra_id,
      'proverbio_explicacion':proverbio_explicacion,
      'frase_aleatorio':frase_aleatorio_id,
      'frase_numero':num_aleatorio_f,
      'frase_dicho':frase_dicho,
      'frase_palabra':frase_palabra,
      'frase_palabra_id':frase_palabra_id,
      'frase_explicacion':frase_explicacion,
      'fecha':datetime.now().strftime('%A, %-d de %B de %Y'),
      'cita_deldia':cita_deldia,
      }
   return render(request, 'index.html', context=context)

def notas(request):
   num_letras = Letra.objects.all().count()
   num_origenes = Origen.objects.all().count()
   num_palabras = Palabra.objects.all().count()
   num_refranes = Refran.objects.all().count()
   num_proverbios = Proverbio.objects.all().count()
   num_frases = Frase.objects.all().count()
   context = {
      'num_letras': num_letras,
      'num_origenes':num_origenes,
      'num_palabras':num_palabras,
      'num_refranes':num_refranes,
      'num_proverbios':num_proverbios,
      'num_frases':num_frases,
      }
   return render(request, 'notas.html', context=context)
#------------------------------------------------------
#  Vistas de Letra
#------------------------------------------------------
class LetraListView(generic.ListView):
   model = Letra
   def get_queryset(self):
      return(
         Letra.objects.all()
         )

class LetraDetailView(generic.DetailView, MultipleObjectMixin):
   model = Letra
   template = "rpyff/letra_detail.html"
   paginate_by = 10

   def get_context_data(self, **kwargs):
      object_list = Palabra.objects.filter(letra=self.get_object()).filter(~Q(estado='r'))
      context = super(LetraDetailView, self).get_context_data(object_list=object_list, **kwargs)
      return context

#------------------------------------------------------
#  Vistas de Origen
#------------------------------------------------------
class OrigenListView(generic.ListView):
   model = Origen
   def get_queryset(self):
      return(
         Origen.objects.filter(estado__exact='a').order_by('fecha')
         )

from django.db.models import Value

class OrigenDetailView(generic.DetailView, MultipleObjectMixin):
   model = Origen
   template = "rpyff/origen_detail.html"
   paginate_by = 20

   def get_context_data(self, **kwargs):
      palabra_list = Palabra.objects.filter(origen=self.get_object()).values('id','palabra','significado')
      refran_list = Refran.objects.filter(origen=self.get_object()).values('id','dicho','explicacion')
      cnt_palabras= Palabra.objects.filter(origen=self.get_object()).count()
      context={}
      context['palabra_list']=palabra_list
      context['refran_list']=refran_list
      context['origen']=self.get_object()
      context['cnt_palabras']=cnt_palabras
      return context

#------------------------------------------------------
#  Vistas de Palabra
#------------------------------------------------------
class PalabraListView(generic.ListView):
   model = Palabra
   paginate_by = 30
   def get_queryset(self):
      return(
         Palabra.objects.filter(~Q(estado='r')).order_by('palabra')
         )
   def get_context_data(self, **kwargs):
      context = super(PalabraListView,self).get_context_data(**kwargs)
      context['letras']=Letra.objects.all
      return context

#class PalabraDetailView(generic.DetailView):
#   model = Palabra

from itertools import chain

class PalabraDetailView(generic.DetailView, MultipleObjectMixin):
   model = Palabra
   template = "rpyff/palabra_detail.html"
   paginate_by = 5

   def get_context_data(self, **kwargs):
      object_list_ref = Refran.objects.filter(palabra=self.get_object()).filter(~Q(estado='r')).annotate(tipo=Value('r'))
      object_list_pro = Proverbio.objects.filter(palabra=self.get_object()).filter(~Q(estado='r')).annotate(tipo=Value('p'))
      object_list_fra = Frase.objects.filter(palabra=self.get_object()).filter(~Q(estado='r')).annotate(tipo=Value('f'))
      object_list_1=[]
      if object_list_ref and object_list_pro:
         object_list_1 = list(chain(object_list_ref,object_list_pro))
      elif object_list_ref:
         object_list_1 = object_list_ref
      elif object_list_pro:
         object_list_1 = object_list_pro
      if object_list_1 and object_list_fra:
         object_list_1 = list(chain(object_list_1,object_list_fra))
      elif object_list_fra:
         object_list_1 = object_list_fra
      #else:
      #   object_list_1 = object_list_ref
      object_list = object_list_1
      context = super(PalabraDetailView, self).get_context_data(object_list=object_list, **kwargs)
      return context

#------------------------------------------------------
#  Vistas de Refrán
#------------------------------------------------------
class RefranListView(generic.ListView):
   model = Refran
   paginate_by = 10
   def get_queryset(self):
      result=Refran.objects.filter(~Q(estado='r'))
      return(
         result.order_by('palabra')
         )
   def get_context_data(self, **kwargs):
      context = super(RefranListView,self).get_context_data(**kwargs)
      Letras=[]
      letras=Letra.objects.all().order_by('letra')
      for letra in letras:
         if letra.refran_set.filter(~Q(estado='r')).count() != 0:
            Letras.append(letra)
      context['letras']=Letras
      Palabras=[]
      palabras=Palabra.objects.filter(~Q(estado='r')).order_by('letra')
      for palabra in palabras:
         refranes=Refran.objects.filter(~Q(estado='r')).filter(palabra__exact=palabra)
         for refran in refranes:
            if refran.palabra:
               Palabras.append(palabra)
               break
      context['palabras']=Palabras
      return context

class RefenRevisionListView(generic.ListView):
   model = Refran
   template_name = 'rpyff/refranes_enrevision_list.html'
   paginate_by = 10
   def get_queryset(self):
      return(
         Refran.objects.filter(estado__exact='r').order_by('palabra')
         )

class RefAprobadosListView(generic.ListView):
   model = Refran
   template_name = 'rpyff/refranes_aprobados_list.html'
   paginate_by = 10
   def get_queryset(self):
      return(
         Refran.objects.filter(estado__exact='a').order_by('palabra')
         )

class RefPublicadosListView(generic.ListView):
   model = Refran
   template_name = 'rpyff/refranes_publicados_list.html'
   paginate_by = 10

   def get_queryset(self):
      return(
         Refran.objects.filter(estado__exact='p').order_by('palabra')
         )

class RefranDetailView(generic.DetailView):
   model = Refran

#------------------------------------------------------
#  Vistas de Proverbio
#------------------------------------------------------
class ProverbioListView(generic.ListView):
   model = Proverbio
   paginate_by = 10
   def get_queryset(self):
      result=Proverbio.objects.filter(~Q(estado='r'))
      return(
         result.order_by('palabra')
         )
   def get_context_data(self, **kwargs):
      context = super(ProverbioListView,self).get_context_data(**kwargs)
      Letras=[]
      letras=Letra.objects.all().order_by('letra')
      for letra in letras:
         if letra.proverbio_set.filter(~Q(estado='r')).count() != 0:
            Letras.append(letra)
      context['letras']=Letras
      Palabras=[]
      palabras=Palabra.objects.filter(~Q(estado='r')).order_by('letra')
      for palabra in palabras:
         proverbios=Proverbio.objects.filter(palabra__exact=palabra).filter(~Q(estado='r'))
         for proverbio in proverbios:
            if proverbio.palabra:
               Palabras.append(palabra)
               break
      context['palabras']=Palabras
      return context

class ProverbioDetailView(generic.DetailView):
   model = Proverbio

#------------------------------------------------------
#  Vistas de Frase
#------------------------------------------------------
class FraseListView(generic.ListView):
   model = Frase
   paginate_by = 10
   def get_queryset(self):
      result=Frase.objects.filter(~Q(estado='r'))
      return(
         result.order_by('palabra')
         )
   def get_context_data(self, **kwargs):
      context = super(FraseListView,self).get_context_data(**kwargs)
      Letras=[]
      letras=Letra.objects.all().order_by('letra')
      for letra in letras:
         if letra.frase_set.filter(~Q(estado='r')).count() != 0:
            Letras.append(letra)
      context['letras']=Letras
      Palabras=[]
      palabras=Palabra.objects.all().order_by('letra')
      for palabra in palabras:
         frases=Frase.objects.filter(palabra__exact=palabra).filter(~Q(estado='r'))
         for frase in frases:
            if frase.palabra:
               Palabras.append(palabra)
               break
      context['palabras']=Palabras
      return context

class FraseDetailView(generic.DetailView):
   model = Frase

#------------------------------------------------------------
#  Vistas de Palabras y Refranes Creados por Usuario
#------------------------------------------------------------
from django.contrib.auth.mixins import LoginRequiredMixin

class PalabrasCreadasListView(LoginRequiredMixin, generic.ListView):

   model = Palabra
   template_name = 'rpyff/palabrascreadas_por_usuario.html'
   paginate_by = 10

   def get_queryset(self):
      return (
         Palabra.objects.filter(creador=self.request.user).order_by('palabra')
         )

class RefranesCreadosListView(LoginRequiredMixin, generic.ListView):

   model = Refran
   template_name = 'rpyff/refranescreados_por_usuario.html'
   paginate_by = 10

   def get_queryset(self):
      return(
         Refran.objects.filter(creador=self.request.user).order_by('palabra')
         )

class ProverbiosCreadosListView(LoginRequiredMixin, generic.ListView):

   model = Proverbio
   template_name = 'rpyff/proverbioscreados_por_usuario.html'
   paginate_by = 10

   def get_queryset(self):
      return(
         Proverbio.objects.filter(creador=self.request.user).order_by('palabra')
         )

class FrasesCreadosListView(LoginRequiredMixin, generic.ListView):

   model = Frase
   template_name = 'rpyff/frasescreadas_por_usuario.html'
   paginate_by = 10

   def get_queryset(self):
      return(
         Frase.objects.filter(creador=self.request.user).order_by('palabra')
         )

class RefranesenRevisionListView(LoginRequiredMixin, generic.ListView):

   model = Refran
   template_name = 'rpyff/refranesenrevision_de_usuario.html'
   paginate_by = 10

   def get_queryset(self):
      return(
         Refran.objects.filter(creador=self.request.user).filter(estado__exact='r').order_by('palabra')
         )
class RefranesAprobadosListView(LoginRequiredMixin, generic.ListView):

   model = Refran
   template_name = 'rpyff/refranesaprobados_de_usuario.html'
   paginate_by = 10

   def get_queryset(self):
      return(
         Refran.objects.filter(creador=self.request.user).filter(estado__exact='a').order_by('palabra')
         )
class RefranesPublicadosListView(LoginRequiredMixin, generic.ListView):

   model = Refran
   template_name = 'rpyff/refranespublicados_de_usuario.html'
   paginate_by = 10

   def get_queryset(self):
      return(
         Refran.objects.filter(creador=self.request.user).filter(estado__exact='p').order_by('palabra')
         )

#------------------------------------------------------------
#  Vistas de Letras, Orígenes, Palabras y Refranes Totales
#------------------------------------------------------------
class TodasLetrasListView(LoginRequiredMixin, generic.ListView):

   model = Letra
   template_name = 'rpyff/todas_letras.html'

   def get_queryset(self):
      return(
         Letra.objects.all()
         )

class TodosOrigenesListView(LoginRequiredMixin, generic.ListView):
   model = Origen
   template_name = 'rpyff/todos_origenes.html'

   def get_queryset(self):
      return(
         Origen.objects.all().order_by('fecha')
         )

class TodasPalabrasListView(LoginRequiredMixin, generic.ListView):
   model = Palabra
   template_name = 'rpyff/todas_palabras.html'
   paginate_by = 30

   def get_queryset(self):
      return(
         Palabra.objects.all().order_by('palabra')
         )
   def get_context_data(self, **kwargs):
      context = super(TodasPalabrasListView,self).get_context_data(**kwargs)
      context['letras']=Letra.objects.all
      return context

class TodosRefranesListView(LoginRequiredMixin, generic.ListView):
   model = Refran
   template_name = 'rpyff/todos_refranes.html'
   paginate_by = 10

   def get_queryset(self):
      return(
         Refran.objects.all().order_by('palabra')
         )
   def get_context_data(self, **kwargs):
      context = super(TodosRefranesListView,self).get_context_data(**kwargs)
      Letras=[]
      letras=Letra.objects.all().order_by('letra')
      for letra in letras:
         if letra.refran_set.filter(~Q(estado='r')).count() != 0:
            Letras.append(letra)
      context['letras']=Letras
      Palabras=[]
      palabras=Palabra.objects.all().order_by('letra')
      for palabra in palabras:
         refranes=Refran.objects.filter(palabra__exact=palabra)
         for refran in refranes:
            if refran.palabra:
               Palabras.append(palabra)
               break
      context['palabras']=Palabras
      return context

class TodosProverbiosListView(LoginRequiredMixin, generic.ListView):
   model = Proverbio
   template_name = 'rpyff/todos_proverbios.html'
   paginate_by = 10

   def get_queryset(self):
      return(
         Proverbio.objects.all().order_by('palabra')
         )
   def get_context_data(self, **kwargs):
      context = super(TodosProverbiosListView,self).get_context_data(**kwargs)
      Letras=[]
      letras=Letra.objects.all().order_by('letra')
      for letra in letras:
         if letra.proverbio_set.filter(~Q(estado='r')).count() != 0:
            Letras.append(letra)
      context['letras']=Letras
      Palabras=[]
      palabras=Palabra.objects.all().order_by('letra')
      for palabra in palabras:
         proverbios=Proverbio.objects.filter(palabra__exact=palabra)
         for proverbio in proverbios:
            if proverbio.palabra:
               Palabras.append(palabra)
               break
      context['palabras']=Palabras
      return context

class TodasFrasesListView(LoginRequiredMixin, generic.ListView):
   model = Frase
   template_name = 'rpyff/todas_frases.html'
   paginate_by = 10

   def get_queryset(self):
      return(
         Frase.objects.all().order_by('palabra')
         )
   def get_context_data(self, **kwargs):
      context = super(TodasFrasesListView,self).get_context_data(**kwargs)
      Letras=[]
      letras=Letra.objects.all().order_by('letra')
      for letra in letras:
         if letra.frase_set.filter(~Q(estado='r')).count() != 0:
            Letras.append(letra)
      context['letras']=Letras
      Palabras=[]
      palabras=Palabra.objects.all().order_by('letra')
      for palabra in palabras:
         frases=Frase.objects.filter(palabra__exact=palabra)
         for frase in frases:
            if frase.palabra:
               Palabras.append(palabra)
               break
      context['palabras']=Palabras
      return context

#from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Palabra, Refran
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect

#------------------------------------------------------------
#  Vistas de edición de Letras
#------------------------------------------------------------
class LetraNueva(PermissionRequiredMixin, CreateView):
   model = Letra
   fields=['letra']
   permission_required='refran.add_letra'

class LetraBorra(PermissionRequiredMixin,DeleteView):
   model = Letra
   success_url = reverse_lazy('letras')
   permission_required='refran.delete_letra'

   def form_valid(self, form):
      try:
         self.object.delete()
         return HttpResponseRedirect(self.success_url)
      except:
         reverse("letra-borra", kwargs={"pk":self.object.pk})

#------------------------------------------------------------
#  Vistas de edición de Palabras
#------------------------------------------------------------
def PalabraNueva(request):
   if request.method=="POST":
      form=PalabraForm(request.POST)
      if form.is_valid():
         palabra=form.save(commit=False)
         palabra.creador=request.user
#         palabra.fecha=date.today
         palabra.save()
         success_url = reverse_lazy('palabra-detalle', kwargs={"pk":palabra.pk})
         return redirect(success_url)
   else:
      form=PalabraForm()
   return render(request,'rpyff/palabra_nueva.html', {'form':form})

   def no_repetida(self):
      buscada=Palabra.objects.filter(palabra__exact=self.palabra)
      if buscada:
         return(False)
      return(True)

class PalabraActualiza(PermissionRequiredMixin,UpdateView):
   model = Palabra
   fields=['palabra', 'significado', 'letra', 'fecha', 'origen', 'creador', 'estado']
   permission_required='refran.change_palabra'

class PalabraBorra(PermissionRequiredMixin,DeleteView):
   model = Palabra
   success_url = reverse_lazy('palabras')
   permission_required='refran.delete_palabra'

   def form_valid(self, form):
      try:
         self.object.delete()
         return HttpResponseRedirect(self.success_url)
      except:
         reverse("palabra-borra", kwargs={"pk":self.object.pk})

#------------------------------------------------------------
#  Vistas de edición de Refranes
#------------------------------------------------------------
def RefranNuevo(request):
   if request.method=="POST":
      form=RefranForm(request.POST)
      if form.is_valid():
         refran=form.save(commit=False)
         refran.creador=request.user
#         palabra.fecha=date.today
         estado=request.POST.get('estado', None)
         fecha=datetime.now().today()
         if estado == 'r':
            refran.fecha=fecha
         if estado == 'a':
            refran.fecha=fecha
            refran.fechaaprobacion=fecha
         if estado == 'p':
            refran.fecha=fecha
            refran.fechaaprobacion=fecha
            refran.fechapublicacion=fecha
         refran.save()
         otraspalabras=request.POST.getlist('otraspalabras', None)
         for palabra in otraspalabras:
            refran.otraspalabras.add(palabra)
         success_url = reverse_lazy('refran-detalle', kwargs={"pk":refran.pk})
         return redirect(success_url)
   else:
      form=RefranForm()
   return render(request,'rpyff/refran_nuevo.html', {'form':form})

class RefranActualiza(PermissionRequiredMixin,UpdateView):
   model = Refran
   fields=['dicho', 'explicacion', 'fecha', 'fechaaprobacion', 'fechapublicacion', 'estado', 'letra', 'palabra', 'otraspalabras','origen', 'creador']
   permission_required='refran.change_refran'

class RefranBorra(PermissionRequiredMixin,DeleteView):
   model = Refran
   success_url = reverse_lazy('refranes')
   permission_required='refran.delete_refran'

   def form_valid(self, form):
      try:
         self.object.delete()
         return HttpResponseRedirect(self.success_url)
      except:
         reverse("refran-borra", kwargs={"pk":self.object.pk})

#------------------------------------------------------------
#  Vistas de edición de Proverbios
#------------------------------------------------------------
def ProverbioNuevo(request):
   if request.method=="POST":
      form=ProverbioForm(request.POST)
      if form.is_valid():
         proverbio=form.save(commit=False)
         proverbio.creador=request.user
#         palabra.fecha=date.today
         estado=request.POST.get('estado', None)
         fecha=datetime.now().today()
         if estado == 'r':
            proverbio.fecha=fecha
         if estado == 'a':
            proverbio.fecha=fecha
            proverbio.fechaaprobacion=fecha
         if estado == 'p':
            proverbio.fecha=fecha
            proverbio.fechaaprobacion=fecha
            proverbio.fechapublicacion=fecha
         proverbio.save()
         otraspalabras=request.POST.getlist('otraspalabras', None)
         for palabra in otraspalabras:
            proverbio.otraspalabras.add(palabra)
         success_url = reverse_lazy('proverbio-detalle', kwargs={"pk":proverbio.pk})
         return redirect(success_url)
   else:
      form=ProverbioForm()
   return render(request,'rpyff/proverbio_nuevo.html', {'form':form})

class ProverbioActualiza(PermissionRequiredMixin,UpdateView):
   model = Proverbio
   fields=['dicho', 'explicacion', 'fecha', 'fechaaprobacion', 'fechapublicacion', 'estado', 'letra', 'palabra', 'otraspalabras', 'origen', 'creador']
   permission_required='rpyff.change_proverbio'

class ProverbioBorra(PermissionRequiredMixin,DeleteView):
   model = Proverbio
   success_url = reverse_lazy('proverbios')
   permission_required='rpyff.delete_proverbio'

   def form_valid(self, form):
      try:
         self.object.delete()
         return HttpResponseRedirect(self.success_url)
      except:
         reverse("proverbio-borra", kwargs={"pk":self.object.pk})

#------------------------------------------------------------
#  Vistas de edición de Frases
#------------------------------------------------------------
def FraseNueva(request):
   if request.method=="POST":
      form=FraseForm(request.POST)
      if form.is_valid():
         frase=form.save(commit=False)
         frase.creador=request.user
#         palabra.fecha=date.today
         estado=request.POST.get('estado', None)
         fecha=datetime.now().today()
         if estado == 'r':
            frase.fecha=fecha
         if estado == 'a':
            frase.fecha=fecha
            frase.fechaaprobacion=fecha
         if estado == 'p':
            frase.fecha=fecha
            frase.fechaaprobacion=fecha
            frase.fechapublicacion=fecha
         frase.save()
         otraspalabras=request.POST.getlist('otraspalabras', None)
         for palabra in otraspalabras:
            frase.otraspalabras.add(palabra)
         success_url = reverse_lazy('frase-detalle', kwargs={"pk":frase.pk})
         return redirect(success_url)
   else:
      form=FraseForm()
   return render(request,'rpyff/frase_nueva.html', {'form':form})

class FraseActualiza(PermissionRequiredMixin,UpdateView):
   model = Frase
   fields=['dicho', 'explicacion', 'fecha', 'fechaaprobacion', 'fechapublicacion', 'estado', 'letra', 'palabra', 'otraspalabras', 'origen', 'creador']
   permission_required='rpyff.change_frase'

class FraseBorra(PermissionRequiredMixin,DeleteView):
   model = Frase
   success_url = reverse_lazy('frases')
   permission_required='rpyff.delete_frase'

   def form_valid(self, form):
      try:
         self.object.delete()
         return HttpResponseRedirect(self.success_url)
      except:
         reverse("frase-borra", kwargs={"pk":self.object.pk})

from django.shortcuts import get_object_or_404
#------------------------------------------------------------
#  Vistas de filtros
#------------------------------------------------------------
class PalabrasLetraListView(generic.ListView):
   model = Palabra
   template_name = 'rpyff/palabras_de_letra.html'
   paginate_by = 30
   
   def get_queryset(self):
       self.letra=get_object_or_404(Letra,id=self.kwargs["pk"])
       return Palabra.objects.filter(letra=self.letra).filter(~Q(estado='r'))

   def get_context_data(self, **kwargs):
      context = super(PalabrasLetraListView,self).get_context_data(**kwargs)
      context['letras']=Letra.objects.all
      context['letra']=self.letra
      return context

class PalabrasOrigenListView(generic.ListView):
   model = Palabra
   template_name = 'rpyff/palabras_de_origen.html'
   paginate_by = 10
   
   def get_queryset(self):
       self.origen=get_object_or_404(Origen,id=self.kwargs["pk"])
       return Palabra.objects.filter(origen=self.origen).filter(~Q(estado='r'))

   def get_context_data(self, **kwargs):
      context = super(PalabrasOrigenListView,self).get_context_data(**kwargs)
      context['origen']=self.origen
      return context

class RefranesOrigenListView(generic.ListView):
   model = Refran
   template_name = 'rpyff/refranes_de_origen.html'
   paginate_by = 10
   
   def get_queryset(self):
       self.origen=get_object_or_404(Origen,id=self.kwargs["pk"])
       return Refran.objects.filter(origen=self.origen).filter(~Q(estado='r'))

   def get_context_data(self, **kwargs):
      context = super(RefranesOrigenListView,self).get_context_data(**kwargs)
      context['origen']=self.origen
      return context

class ProverbiosOrigenListView(generic.ListView):
   model = Proverbio
   template_name = 'rpyff/proverbios_de_origen.html'
   paginate_by = 10
   
   def get_queryset(self):
       self.origen=get_object_or_404(Origen,id=self.kwargs["pk"])
       return Proverbio.objects.filter(origen=self.origen).filter(~Q(estado='r'))

   def get_context_data(self, **kwargs):
      context = super(ProverbiosOrigenListView,self).get_context_data(**kwargs)
      context['origen']=self.origen
      return context

class FrasesOrigenListView(generic.ListView):
   model = Frase
   template_name = 'rpyff/frases_de_origen.html'
   paginate_by = 10
   
   def get_queryset(self):
       self.origen=get_object_or_404(Origen,id=self.kwargs["pk"])
       return Frase.objects.filter(origen=self.origen).filter(~Q(estado='r'))

   def get_context_data(self, **kwargs):
      context = super(FrasesOrigenListView,self).get_context_data(**kwargs)
      context['origen']=self.origen
      return context

class RefranesPalabraListView(generic.ListView):
   model = Refran
   template_name = 'rpyff/refranes_de_palabra.html'
   paginate_by = 10
   
   def get_queryset(self):
       self.palabra=get_object_or_404(Palabra,id=self.kwargs["pk"])
       return Refran.objects.filter(palabra=self.palabra).filter(~Q(estado='r'))

   def get_context_data(self, **kwargs):
      context = super(RefranesPalabraListView,self).get_context_data(**kwargs)
      Letras=[]
      letras=Letra.objects.all().order_by('letra')
      for letra in letras:
         if letra.refran_set.filter(~Q(estado='r')).count() != 0:
            Letras.append(letra)
      context['letras']=Letras
      Palabras=[]
      palabras=Palabra.objects.filter(~Q(estado='r'))
      for palabra in palabras:
         refranes=Refran.objects.filter(palabra__exact=palabra).filter(~Q(estado='r'))
         for refran in refranes:
            if refran.palabra:
               Palabras.append(palabra)
               break
      context['palabras']=Palabras
      context['palabra']=self.palabra
      return context

class ProverbiosPalabraListView(generic.ListView):
   model = Proverbio
   template_name = 'rpyff/proverbios_de_palabra.html'
   paginate_by = 10
   
   def get_queryset(self):
       self.palabra=get_object_or_404(Palabra,id=self.kwargs["pk"])
       return Proverbio.objects.filter(palabra=self.palabra).filter(~Q(estado='r'))

   def get_context_data(self, **kwargs):
      context = super(ProverbiosPalabraListView,self).get_context_data(**kwargs)
      Letras=[]
      letras=Letra.objects.all().order_by('letra')
      for letra in letras:
         if letra.proverbio_set.filter(~Q(estado='r')).count() != 0:
            Letras.append(letra)
      context['letras']=Letras
      Palabras=[]
      palabras=Palabra.objects.filter(~Q(estado='r')).order_by('letra')
      for palabra in palabras:
         proverbios=Proverbio.objects.filter(palabra__exact=palabra).filter(~Q(estado='r'))
         for proverbio in proverbios:
            if proverbio.palabra:
               Palabras.append(palabra)
               break
      context['palabras']=Palabras
      context['palabra']=self.palabra
      return context

class FrasesPalabraListView(generic.ListView):
   model = Frase
   template_name = 'rpyff/frases_de_palabra.html'
   paginate_by = 10
   
   def get_queryset(self):
       self.palabra=get_object_or_404(Palabra,id=self.kwargs["pk"])
       return Frase.objects.filter(palabra=self.palabra).filter(~Q(estado='r'))

   def get_context_data(self, **kwargs):
      context = super(FrasesPalabraListView,self).get_context_data(**kwargs)
      Letras=[]
      letras=Letra.objects.all().order_by('letra')
      for letra in letras:
         if letra.frase_set.filter(~Q(estado='r')).count() != 0:
            Letras.append(letra)
      context['letras']=Letras
      Palabras=[]
      palabras=Palabra.objects.filter(~Q(estado='r')).order_by('letra')
      for palabra in palabras:
         frases=Frase.objects.filter(palabra__exact=palabra).filter(~Q(estado='r'))
         for frase in frases:
            if frase.palabra:
               Palabras.append(palabra)
               break
      context['palabras']=Palabras
      context['palabra']=self.palabra
      return context

class RefranesLetraListView(generic.ListView):
   model = Refran
   template_name = 'rpyff/refranes_de_letra.html'
   paginate_by = 10
   
   def get_queryset(self):
       self.letra=get_object_or_404(Letra,id=self.kwargs["pk"])
       palabras=Palabra.objects.filter(letra=self.letra).filter(~Q(estado='r'))
       return Refran.objects.filter(palabra__in=palabras).filter(~Q(estado='r'))

   def get_context_data(self, **kwargs):
      context = super(RefranesLetraListView,self).get_context_data(**kwargs)
      Letras=[]
      letras=Letra.objects.all().order_by('letra')
      for letra in letras:
         if letra.refran_set.filter(~Q(estado='r')).count() != 0:
            Letras.append(letra)
      context['letras']=Letras
      Palabras=[]
      palabras=Palabra.objects.filter(letra=self.kwargs["pk"]).filter(~Q(estado='r'))
      for palabra in palabras:
         refranes=Refran.objects.filter(palabra__exact=palabra).filter(~Q(estado='r'))
         for refran in refranes:
            if refran.palabra:
               Palabras.append(palabra)
               break
      context['palabras']=Palabras
      context['letra']=self.letra
      return context

class ProverbiosLetraListView(generic.ListView):
   model = Proverbio
   template_name = 'rpyff/proverbios_de_letra.html'
   paginate_by = 10
   
   def get_queryset(self):
       self.letra=get_object_or_404(Letra,id=self.kwargs["pk"])
       palabras=Palabra.objects.filter(letra=self.letra).filter(~Q(estado='r'))
       return Proverbio.objects.filter(palabra__in=palabras).filter(~Q(estado='r'))

   def get_context_data(self, **kwargs):
      context = super(ProverbiosLetraListView,self).get_context_data(**kwargs)
      Letras=[]
      letras=Letra.objects.all().order_by('letra')
      for letra in letras:
         if letra.proverbio_set.filter(~Q(estado='r')).count() != 0:
            Letras.append(letra)
      context['letras']=Letras
      Palabras=[]
      palabras=Palabra.objects.filter(letra=self.kwargs["pk"]).filter(~Q(estado='r'))
      for palabra in palabras:
         proverbios=Proverbio.objects.filter(palabra__exact=palabra).filter(~Q(estado='r'))
         for proverbio in proverbios:
            if proverbio.palabra:
               Palabras.append(palabra)
               break
      context['palabras']=Palabras
      context['letra']=self.letra
      return context

class FrasesLetraListView(generic.ListView):
   model = Frase
   template_name = 'rpyff/frases_de_letra.html'
   paginate_by = 10
   
   def get_queryset(self):
       self.letra=get_object_or_404(Letra,id=self.kwargs["pk"])
       palabras=Palabra.objects.filter(letra=self.letra).filter(~Q(estado='r'))
       return Frase.objects.filter(palabra__in=palabras).filter(~Q(estado='r'))

   def get_context_data(self, **kwargs):
      context = super(FrasesLetraListView,self).get_context_data(**kwargs)
      Letras=[]
      letras=Letra.objects.all().order_by('letra')
      for letra in letras:
         if letra.frase_set.filter(~Q(estado='r')).count() != 0:
            Letras.append(letra)
      context['letras']=Letras
      Palabras=[]
      palabras=Palabra.objects.filter(letra=self.kwargs["pk"]).filter(~Q(estado='r'))
      for palabra in palabras:
         frases=Frase.objects.filter(palabra__exact=palabra).filter(~Q(estado='r'))
         for frase in frases:
            if frase.palabra:
               Palabras.append(palabra)
               break
      context['palabras']=Palabras
      context['letra']=self.letra
      return context

#------------------------------------------------------------
#  Vistas de filtros para todas y todos (Administración)
#------------------------------------------------------------
class TodasPalabrasLetraListView(generic.ListView):
   model = Palabra
   template_name = 'rpyff/todas_palabras_de_letra.html'
   paginate_by = 30
   
   def get_queryset(self):
       self.letra=get_object_or_404(Letra,id=self.kwargs["pk"])
       return Palabra.objects.filter(letra=self.letra)

   def get_context_data(self, **kwargs):
      context = super(TodasPalabrasLetraListView,self).get_context_data(**kwargs)
      context['letras']=Letra.objects.all
      context['letra']=self.letra
      return context

class TodosRefranesPalabraListView(generic.ListView):
   model = Refran
   template_name = 'rpyff/todos_refranes_de_palabra.html'
   paginate_by = 10
   
   def get_queryset(self):
       self.palabra=get_object_or_404(Palabra,id=self.kwargs["pk"])
       return Refran.objects.filter(palabra=self.palabra)

   def get_context_data(self, **kwargs):
      context = super(TodosRefranesPalabraListView,self).get_context_data(**kwargs)
      Letras=[]
      letras=Letra.objects.all().order_by('letra')
      for letra in letras:
         if letra.refran_set.all().count() != 0:
            Letras.append(letra)
      context['letras']=Letras
      context['palabras']=Palabra.objects.all
      Palabras=[]
      palabras=Palabra.objects.all()
      for palabra in palabras:
         refranes=Refran.objects.filter(palabra__exact=palabra)
         for refran in refranes:
            if refran.palabra:
               Palabras.append(palabra)
               break
      context['palabras']=Palabras
      context['palabra']=self.palabra
      return context

class TodosProverbiosPalabraListView(generic.ListView):
   model = Proverbio
   template_name = 'rpyff/todos_proverbios_de_palabra.html'
   paginate_by = 10
   
   def get_queryset(self):
       self.palabra=get_object_or_404(Palabra,id=self.kwargs["pk"])
       return Proverbio.objects.filter(palabra=self.palabra)

   def get_context_data(self, **kwargs):
      context = super(TodosProverbiosPalabraListView,self).get_context_data(**kwargs)
      Letras=[]
      letras=Letra.objects.all().order_by('letra')
      for letra in letras:
         if letra.proverbio_set.all().count() != 0:
            Letras.append(letra)
      context['letras']=Letras
      Palabras=[]
      palabras=Palabra.objects.all()
      for palabra in palabras:
         proverbios=Proverbio.objects.filter(palabra__exact=palabra)
         for proverbio in proverbios:
            if proverbio.palabra:
               Palabras.append(palabra)
               break
      context['palabras']=Palabras
      context['palabra']=self.palabra
      return context

class TodasFrasesPalabraListView(generic.ListView):
   model = Frase
   template_name = 'rpyff/todas_frases_de_palabra.html'
   paginate_by = 10
   
   def get_queryset(self):
       self.palabra=get_object_or_404(Palabra,id=self.kwargs["pk"])
       return Frase.objects.filter(palabra=self.palabra)

   def get_context_data(self, **kwargs):
      context = super(TodasFrasesPalabraListView,self).get_context_data(**kwargs)
      Letras=[]
      letras=Letra.objects.all().order_by('letra')
      for letra in letras:
         if letra.frase_set.all().count() != 0:
            Letras.append(letra)
      context['letras']=Letras
      Palabras=[]
      palabras=Palabra.objects.all()
      for palabra in palabras:
         frases=Frase.objects.filter(palabra__exact=palabra)
         for frase in frases:
            if frase.palabra:
               Palabras.append(palabra)
               break
      context['palabras']=Palabras
      context['palabra']=self.palabra
      return context

class TodosRefranesLetraListView(generic.ListView):
   model = Refran
   template_name = 'rpyff/todos_refranes_de_letra.html'
   paginate_by = 10
   
   def get_queryset(self):
       self.letra=get_object_or_404(Letra,id=self.kwargs["pk"])
       palabras=Palabra.objects.filter(letra=self.letra)
       return Refran.objects.filter(palabra__in=palabras)

   def get_context_data(self, **kwargs):
      context = super(TodosRefranesLetraListView,self).get_context_data(**kwargs)
      Letras=[]
      letras=Letra.objects.all().order_by('letra')
      for letra in letras:
         if letra.refran_set.all().count() != 0:
            Letras.append(letra)
      context['letras']=Letras
      Palabras=[]
      palabras=Palabra.objects.filter(letra=self.kwargs["pk"])
      for palabra in palabras:
         refranes=Refran.objects.filter(palabra__exact=palabra)
         for refran in refranes:
            if refran.palabra:
               Palabras.append(palabra)
               break
      context['palabras']=Palabras
      context['letra']=self.letra
      return context

class TodosProverbiosLetraListView(generic.ListView):
   model = Proverbio
   template_name = 'rpyff/todos_proverbios_de_letra.html'
   paginate_by = 10
   
   def get_queryset(self):
       self.letra=get_object_or_404(Letra,id=self.kwargs["pk"])
       palabras=Palabra.objects.filter(letra=self.letra)
       return Proverbio.objects.filter(palabra__in=palabras)

   def get_context_data(self, **kwargs):
      context = super(TodosProverbiosLetraListView,self).get_context_data(**kwargs)
      Letras=[]
      letras=Letra.objects.all().order_by('letra')
      for letra in letras:
         if letra.proverbio_set.all().count() != 0:
            Letras.append(letra)
      context['letras']=Letras
      Palabras=[]
      palabras=Palabra.objects.filter(letra=self.kwargs["pk"])
      for palabra in palabras:
         proverbios=Proverbio.objects.filter(palabra__exact=palabra)
         for proverbio in proverbios:
            if proverbio.palabra:
               Palabras.append(palabra)
               break
      context['palabras']=Palabras
      context['letra']=self.letra
      return context

class TodasFrasesLetraListView(generic.ListView):
   model = Frase
   template_name = 'rpyff/todas_frases_de_letra.html'
   paginate_by = 10
   
   def get_queryset(self):
       self.letra=get_object_or_404(Letra,id=self.kwargs["pk"])
       palabras=Palabra.objects.filter(letra=self.letra)
       return Frase.objects.filter(palabra__in=palabras)

   def get_context_data(self, **kwargs):
      context = super(TodasFrasesLetraListView,self).get_context_data(**kwargs)
      Letras=[]
      letras=Letra.objects.all().order_by('letra')
      for letra in letras:
         if letra.frase_set.all().count() != 0:
            Letras.append(letra)
      context['letras']=Letras
      Palabras=[]
      palabras=Palabra.objects.filter(letra=self.kwargs["pk"])
      for palabra in palabras:
         frases=Frase.objects.filter(palabra__exact=palabra)
         for frase in frases:
            if frase.palabra:
               Palabras.append(palabra)
               break
      context['palabras']=Palabras
      context['letra']=self.letra
      return context

#------------------------------------------------------------
#  Vistas Extras
#------------------------------------------------------------
def salir(request):
   return render(request, 'rpyff/salir.html')
#------------------------------------------------------------
#  Fin de definición de Vistas
#------------------------------------------------------------

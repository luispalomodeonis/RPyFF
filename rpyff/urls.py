
#------------------------------------------------------
#  Sección de importación de módulos
#------------------------------------------------------
from . import views
from django.urls import path

#------------------------------------------------------
#  Paths generales de acceso a instancias
#------------------------------------------------------
urlpatterns = [
   path('', views.index, name='index'),
   path('letras/', views.LetraListView.as_view(), name='letras'),
   path('letras/<uuid:pk>', views.LetraDetailView.as_view(), name='letra-detalle'),
   path('origenes/', views.OrigenListView.as_view(), name='origenes'),
   path('origenes/<uuid:pk>', views.OrigenDetailView.as_view(), name='origen-detalle'),
   path('palabras/', views.PalabraListView.as_view(), name='palabras'),
   path('palabras/<uuid:pk>', views.PalabraDetailView.as_view(), name='palabra-detalle'),
   path('refranes/', views.RefranListView.as_view(), name='refranes'),
   path('refranes/<uuid:pk>', views.RefranDetailView.as_view(), name='refran-detalle'),
   path('proverbios/', views.ProverbioListView.as_view(), name='proverbios'),
   path('proverbios/<uuid:pk>', views.ProverbioDetailView.as_view(), name='proverbio-detalle'),
   path('frases/', views.FraseListView.as_view(), name='frases'),
   path('frases/<uuid:pk>', views.FraseDetailView.as_view(), name='frase-detalle'),
   path('notas', views.notas, name='notas'),
   ]

#------------------------------------------------------
#  Paths a instancias filtradas
#------------------------------------------------------
urlpatterns += [
   path('refenrevision/', views.RefenRevisionListView.as_view(), name='refranes-enrevision'),
   path('refaprobados/', views.RefAprobadosListView.as_view(), name='refranes-aprobados'),
   path('refpublicados/', views.RefPublicadosListView.as_view(), name='refranes-publicados'),
   ]

#------------------------------------------------------
#  Paths a instancias de usuario
#------------------------------------------------------
urlpatterns += [
   path('mispalabras/', views.PalabrasCreadasListView.as_view(), name='mis-palabras'),
   path('misrefranes/', views.RefranesCreadosListView.as_view(), name='mis-refranes'),
   path('misproverbios/', views.ProverbiosCreadosListView.as_view(), name='mis-proverbios'),
   path('misfrases/', views.FrasesCreadosListView.as_view(), name='mis-frases'),
   ]

#------------------------------------------------------
#  Paths a instancias de usuario filtradas
#------------------------------------------------------
urlpatterns += [
   path('misenrevision/', views.RefranesenRevisionListView.as_view(), name='mis-refranes-enrevision'),
   path('misaprobados/', views.RefranesAprobadosListView.as_view(), name='mis-refranes-aprobados'),
   path('mispublicados/', views.RefranesPublicadosListView.as_view(), name='mis-refranes-publicados'),
   ]

#------------------------------------------------------
#  Paths a todas las instancias para administradores
#------------------------------------------------------
urlpatterns += [
   path('todasletras/', views.TodasLetrasListView.as_view(), name='todas-letras'),
   path('todosorigenes/', views.TodosOrigenesListView.as_view(), name='todos-origenes'),
   path('todaspalabras/', views.TodasPalabrasListView.as_view(), name='todas-palabras'),
   path('todosrefranes/', views.TodosRefranesListView.as_view(), name='todos-refranes'),
   path('todosproverbios/', views.TodosProverbiosListView.as_view(), name='todos-proverbios'),
   path('todasfrases/', views.TodasFrasesListView.as_view(), name='todas-frases'),
   ]


#------------------------------------------------------
#  Paths a todas con filtros de instancias
#------------------------------------------------------
urlpatterns += [
   path('todaspalabrasletra/<uuid:pk>', views.TodasPalabrasLetraListView.as_view(), name='todas-palabras-letra'),
   path('todosrefranespalabra/<uuid:pk>', views.TodosRefranesPalabraListView.as_view(), name='todos-refranes-palabra'),
   path('todosrefranesletra/<uuid:pk>', views.TodosRefranesLetraListView.as_view(), name='todos-refranes-letra'),
   path('todosproverbiospalabra/<uuid:pk>', views.TodosProverbiosPalabraListView.as_view(), name='todos-proverbios-palabra'),
   path('todosproverbiosletra/<uuid:pk>', views.TodosProverbiosLetraListView.as_view(), name='todos-proverbios-letra'),
   path('todasfrasespalabra/<uuid:pk>', views.TodasFrasesPalabraListView.as_view(), name='todas-frases-palabra'),
   path('todasfrasesletra/<uuid:pk>', views.TodasFrasesLetraListView.as_view(), name='todas-frases-letra'),
   ]
#------------------------------------------------------
#  Paths a operaciones de instancias para autorizados
#------------------------------------------------------
urlpatterns += [
   path('letra/nueva/', views.LetraNueva.as_view(), name='letra-nueva'),
   path('letra/<uuid:pk>/borra/', views.LetraBorra.as_view(), name='letra-borra'),
   path('palabra/nueva/', views.PalabraNueva, name='palabra-nueva'),
   path('palabra/<uuid:pk>', views.PalabraDetailView.as_view(), name='palabra-detalle'),
   path('palabra/<uuid:pk>/actualiza/', views.PalabraActualiza.as_view(), name='palabra-actualiza'),
   path('palabra/<uuid:pk>/borra/', views.PalabraBorra.as_view(), name='palabra-borra'),
   path('refran/nuevo/', views.RefranNuevo, name='refran-nuevo'),
   path('refran/<uuid:pk>/actualiza/', views.RefranActualiza.as_view(), name='refran-actualiza'),
   path('refran/<uuid:pk>/borra/', views.RefranBorra.as_view(), name='refran-borra'),
   path('proverbio/nuevo/', views.ProverbioNuevo, name='proverbio-nuevo'),
   path('proverbio/<uuid:pk>/actualiza/', views.ProverbioActualiza.as_view(), name='proverbio-actualiza'),
   path('proverbio/<uuid:pk>/borra/', views.ProverbioBorra.as_view(), name='proverbio-borra'),
   path('frase/nueva/', views.FraseNueva, name='frase-nueva'),
   path('frase/<uuid:pk>/actualiza/', views.FraseActualiza.as_view(), name='frase-actualiza'),
   path('frase/<uuid:pk>/borra/', views.FraseBorra.as_view(), name='frase-borra'),
   ]

#------------------------------------------------------
#  Paths de filtros de instancias
#------------------------------------------------------
urlpatterns += [
   path('palabrasletra/<uuid:pk>', views.PalabrasLetraListView.as_view(), name='palabras-letra'),
   path('refranesletra/<uuid:pk>', views.RefranesLetraListView.as_view(), name='refranes-letra'),
   path('proverbiosletra/<uuid:pk>', views.ProverbiosLetraListView.as_view(), name='proverbios-letra'),
   path('frasesletra/<uuid:pk>', views.FrasesLetraListView.as_view(), name='frases-letra'),
   path('refranespalabra/<uuid:pk>', views.RefranesPalabraListView.as_view(), name='refranes-palabra'),
   path('proverbiospalabra/<uuid:pk>', views.ProverbiosPalabraListView.as_view(), name='proverbios-palabra'),
   path('frasespalabra/<uuid:pk>', views.FrasesPalabraListView.as_view(), name='frases-palabra'),
   path('palabrasorigen/<uuid:pk>', views.PalabrasOrigenListView.as_view(), name='palabras-origen'),
   path('refranesorigen/<uuid:pk>', views.RefranesOrigenListView.as_view(), name='refranes-origen'),
   path('proverbiosorigen/<uuid:pk>', views.ProverbiosOrigenListView.as_view(), name='proverbios-origen'),
   path('frasesorigen/<uuid:pk>', views.FrasesOrigenListView.as_view(), name='frases-origen'),
   ]

#------------------------------------------------------
#  Paths de búsquedas y contacto
#------------------------------------------------------
urlpatterns += [
   path('buscar', views.buscar, name='buscar'),
   path('buscar_palabra', views.buscar_palabra, name='busca-palabra'),
   path('buscar_significado', views.buscar_significado, name='busca-significado'),
   path('buscar_refran', views.buscar_refran, name='busca-refran'),
   path('buscar_proverbio', views.buscar_proverbio, name='busca-proverbio'),
   path('buscar_frase', views.buscar_frase, name='busca-frase'),
   path('buscar_explicacion', views.buscar_explicacion, name='busca-explicacion'),
   path('buscar_numero', views.buscar_numero, name='busca-numero'),
   path('buscada_palabra/<str:mibusqueda_palabra>', views.PalabraBuscada.as_view(), name='palabra-buscada'),
   path('buscado_significado/<str:mibusqueda_significado>', views.SignificadoBuscado.as_view(), name='significado-buscado'),
   path('buscado_refran/<str:mibusqueda_refran>', views.RefranBuscado.as_view(), name='refran-buscado'),
   path('buscado_proverbio/<str:mibusqueda_proverbio>', views.ProverbioBuscado.as_view(), name='proverbio-buscado'),
   path('buscada_frase/<str:mibusqueda_frase>', views.FraseBuscada.as_view(), name='frase-buscada'),
   path('buscada_explicacion/<str:mibusqueda_explicacion>', views.ExplicacionBuscada.as_view(), name='explicacion-buscada'),
   path('buscado_numero/<str:mibusqueda_numero>', views.NumeroBuscado.as_view(), name='numero-buscado'),
   path('contacto/', views.contacto, name='contacto'),
   #path('gracias/(<str:remitente>)', views.Gracias, name='gracias'),
   path('gracias/', views.Gracias, name='gracias'),
   ]
#------------------------------------------------------
#  Paths de paginas extras
#------------------------------------------------------
urlpatterns += [
   path('salir/', views.salir, name='salir'),
   ]
#------------------------------------------------------
#  Paths de paginas de pruebas
#------------------------------------------------------
#from django.urls import re_path
urlpatterns += [
#   path('nuevo', views.indexnuevo),
#   path('nuevo/', views.indexnuevo),
#   path('new/', views.indexnew),
   ]
#------------------------------------------------------
#  Fin de los Paths
#------------------------------------------------------

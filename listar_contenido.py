print("Inicio")
#from django.contrib.contenttypes.models import ContentType
#import django.contrib.contenttypes.models
import django.contrib.auth.models
print("Importado modelo")
def listado(modulo):
    tree = ""

    for nombre in dir(modulo):
        objeto = getattr(modulo, nombre)
        
        if(callable(objeto)):
            if(isinstance(objeto, type)):
                tree += "class "+nombre+"\n"
                tree += "\n".join("    -"+metodo for metodo in dir(objeto) if(callable(getattr(objeto, metodo)) and metodo[:2]+metodo[-2:] != "____"))
                tree += "\n"
            else:
                tree += "def "+nombre+"\n"

    return tree

#print(listado(django.contrib.contenttypes.models))
print(listado(django.contrib.auth.models))
print("Fin")

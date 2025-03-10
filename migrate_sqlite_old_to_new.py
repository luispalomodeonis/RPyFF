
print("Iniciando la exportación de sqlite antigua a nueva")
print("Importando modelos")

#
#auth_group
#auth_group_permissions
#auth_permission
#auth_user
#auth_user_groups
#auth_user_user_permissions
#
#django_content_type
#
#from django.contrib.auth.models import User
#print("Importando tablas base")
#print("User...")
#objlist = User.objects.all()
#for obj in objlist:
#   obj.save(using='nueva')

#from django.contrib.auth.models import Group
#print("Group...")
#objlist = Group.objects.all()
#for obj in objlist:
#   obj.save(using='nueva')

#from django.contrib.contenttypes.models import ContentType
#print("Content_type...")
#objlist = ContentType.objects.all()
#for obj in objlist:
#   obj.save(using='nueva')

#from django.contrib.auth.models import Permission
#print("Permission...")
#objlist = Permission.objects.all()
#for obj in objlist:
#   obj.save(using='nueva')

#######
#from django.contrib.auth.models import User_groups
#print("User_groups...")
#objlist = User_groups.objects.all()
#for obj in objlist:
#   obj.save(using='nueva')

#from django.contrib.auth.models import UserPermissions
#print("UserPermission...")
#objlist = UserPermissions.objects.all()
#for obj in objlist:
#   obj.save(using='nueva')

#from django.contrib.auth.models import GroupPermissions
#print("GroupPermission...")
#objlist = GroupPermissions.objects.all()
#for obj in objlist:
#   obj.save(using='nueva')

print("Importando Letra")
from rpyff.models import Letra

print("Letras...")
objlist = Letra.objects.all()
for obj in objlist:
   obj.save(using='nueva')

print("Importando Origen")
from rpyff.models import Origen

print("Orígenes..")
objlist = Origen.objects.all()
for obj in objlist:
   obj.save(using='nueva')

print("Importando Palabra")
from rpyff.models import Palabra

print("Palabras...")
objlist = Palabra.objects.all()
for obj in objlist:
   obj.save(using='nueva')

print("Importando Refran")
from rpyff.models import Refran

print("Refranes...")
objlist = Refran.objects.all()
for obj in objlist:
   obj.save(using='nueva')

print("Exportación realizada")


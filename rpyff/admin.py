from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Letra
from .models import Origen

admin.site.register(Letra)
admin.site.register(Origen)


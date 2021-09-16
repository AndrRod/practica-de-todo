from django.contrib import admin
from .models import servicios
# Register your models here.

class serviciosAdm(admin.ModelAdmin):
    # para incluir campos que son solo de lectura
    # registrar los campos solo de lectura, porque estos son autocreados
    readonly_fields = ('creacion', 'actualizacion')


admin.site.register(servicios, serviciosAdm)
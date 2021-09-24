from django.contrib import admin

# Register your models here.
from .models import Post, Categoria

class CategoriaAdm(admin.ModelAdmin):
    # los campos de lectura van a ser igual
    readonly_fields = ('creacion', 'actualizacion')


class PostAdm(admin.ModelAdmin):
    # los campos de lectura van a ser igual
    readonly_fields = ('creacion', 'actualizacion')

admin.site.register(Post, PostAdm)
admin.site.register(Categoria, CategoriaAdm)
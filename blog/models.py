from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = 'categorias'
    
    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    # para manipular imagenes hay que instalar un paquete externo
    # para usar el ImageField hay que descargar o instalar. python -m pip install Pillow

    # upload_to para que se suba a la carpeta media y crear una subcarpeta llamada servicios para emplear las imagenes de este modulo
    # opcional null = True blank = true
    imagen = models.ImageField(upload_to = 'blog', null=True, blank=True)
    
    # si se elimina el autor se elimina todo lo relacionado a el (se estable relaciones un autor relacionado con varios pots relacion de una a varios)
    # heredamos del usuario hacemos relacion entre usuario y post, relacion en cascada
    # on delete en caso de borrarse el autor se borre todo lo relacionado en cascada
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    # un post y una categoria pueden tener varias categiras y varios posts (relacion de varios a varios)
    categorias = models.ManyToManyField(Categoria)
    
    
    # para ordenar por fecha de creación y actualizacion o modificacion
    # auto_now_add : aagrega de manera automatica
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = 'Posts'
    
    def __str__(self):
        return self.titulo
    
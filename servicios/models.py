from django.db import models

# Create your models here.
class servicios(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    # para manipular imagenes hay que instalar un paquete externo
    # para usar el ImageField hay que descargar o instalar. python -m pip install Pillow

    # upload_to para que se suba a la carpeta media y crear una subcarpeta llamada servicios para emplear las imagenes de este modulo
    imagen = models.ImageField(upload_to = 'servicios')
    # para ordenar por fecha de creación y actualizacion o modificacion
    # auto_now_add : aagrega de manera automatica
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = 'servicios'
    
    def __str__(self):
        return self.titulo
    
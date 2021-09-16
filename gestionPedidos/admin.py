from gestionPedidos.models import clientes, articulos, pedidos, Question, Choice
from django.contrib import admin
from django.db import models

# Register your models here.
# hasta ahora solo podemos midificar los usuarios
# dice que registremos nuestros modelos
# para modificar las tablas desde panel de administracion:
# from  gestionPedidos.models import clientes
# admin.site.registrer(clientes)


# como modelar las tablas del panel de administracion:
# de esta forma se crean 3 tablas en clientes y es mas practico trabajar
class clientesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono')
    # si queremos poner un buscador --- search_fields = ('patron de busqueda')
    search_fields= ('nombre', 'telefono')


class articulosAdmin(admin.ModelAdmin):
    # que campos queremos ver
    list_display = ('nombre', 'seccion', 'precio')
    search_fields = ('nombre', 'seccion', 'precio')
    

class pedidosAdmin(admin.ModelAdmin):
    list_display = ('numero', 'fecha')
    # lista filtro que aparece en derecha
    list_filter = ('fecha',)
    # lista horizontal de fechas (detecta años, mes y dias)
    date_hierarchy = 'fecha'
    
    
    

# TabularInline muestra en forma más compacta la informacion
# stackedInline muestra mucho mas campos







class ChoiceInline(admin.TabularInline):
    model = Choice
    # cantidad de opciones
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # se puede alterar el orden de las filas o puestos con fields
    # fields = ['pub_date', 'question_text']

    # también podriamos dividis los campos con fieldsets el primer parametro sería el titulo (que si ponemos none no va ninguno)
    # también podemos agregar una clase collapse que sirve para cuando hay demasiada información se pliegue
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Información de Fecha', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # esto es para que cuando uno cree el objeto Question puede hacerlo con los choices
    inlines = [ChoiceInline]
    # la forma de mostrar la información en la pantalla inicial pregunta y fecha (similar al str que colocamos en el models.py)
    list_display = ('question_text', 'pub_date', 'publicado_recientemente')

    # buscador lateral por fecha de publicación
    list_filter = ['pub_date']
    # buscador por pregunta
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)

admin.site.register(clientes, clientesAdmin)
admin.site.register(articulos, articulosAdmin)
admin.site.register(pedidos, pedidosAdmin)
# admin.site.register(Question)
# admin.site.register(Choice)   
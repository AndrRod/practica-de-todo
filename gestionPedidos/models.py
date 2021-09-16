from django.db import models
from django.db.models.base import Model

# Instalar PostgreSqul.
# una vez instalado acceder a PGadmin 4
# desde el lenguaje sql
#  para crear una base de datos ir a QUERY TOOL y colocar create database nombre
# instalar la libreria psycopg2 para conectar la base de datos y el proyecto
# en el directorio del proyecto: python pip install psycopg2



# Create your models here.

# django-admin startproject (nombre cualquiera) TiendaOnline - para comenzar proyecto
# cd TiendaOnline - entrar en la carpeta para poder acceder a manage.py
# python manage.py startapp (nombre cualqiera) gestionPedidos - para crear aplicacion

# este modelo marca la estructura de nuestra base de datos
# hay que registrar la aplicacion ('gestionPedidos') en el proyecto es decir en settings.py (INSTALLED_APPS)


# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     # aca se instalan las nuevas aplicañciones
#     'gestionPedidos', <------------------------- aca en lo ultimo vamos registrando
# ]

# tambien hay que hacer la migracion de la base de datos (python manage.py makemigrations)
# como metemos las tablas en sql desde django, con el siguiente comando (python manage.py sqlmigrate gestionPedidos 0001)
# despues salen en terminal las instrucciones, crea las tablas con sus propiedades
# ademas hay que pedir que este codigo sql se utilice para meter esas tablas en nuestra base de datos (python manage.py migrate)

# y comprobar si fue registrado correctamente la aplicacion (python manage.py check gestionPedidos)

# para manipular la base de datos desde consola hay que abrir el server
# pyhon manage.py shell
# from gestionPedidos.models import articulos
# art = articulos(nombre='', seccion ='', precio = )
# art.save()
# o sino directamente se guarda con la siguiente:
# art3 = articulos.objects.create(nombre='taladro', seccion = 'ferreteria', precio=65)
# como cambiar un dato:
#  art2.precio = 95
#  art2.save()
# para borrar: hacemos una variable de un archivo (con la id)
# art5 = articulos.objects.get(id=2)
# art5.delete()
# almacenar en una lista todos los articulos:
# lista=articulos.objects.all()
# 
# para que django conecte con nuestra base de datos tenemos que:
# bajar postgreSQL
# una vez instalado acceder a PGadmin 4
# en postgreSQL - Queery Tool - en consola colocar con lenguaje sql: create database nombre_de_base_de_datos
# hacer la siguiente instalacion para que se pueda conectar con la base de datos:
#  pip install psycopg2 en la carpeta del proyecto
# tenemos que modificar la configuracion de la base de datos de django para poder conectar el proyecto y  la base de datos (settings.py - DATABASE -)


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2', <------ esta linea colocar
#         'NAME': 'articulosclientes',
#         'USER': 'postgres',
#         'PASSWORD': 'Lgante03',
#         'HOST': '127.0.0.1',
#         'DATABASE_PORT': '5432',
#     }
# }

# Para hacer las migraciones de nuestro proyecto a base de datos:
# python manage.py makemigrations

# hay que ejecutar la migracion para ver los efectos si hicimos modificaciones:
# python manage.py migrate

# nuevamente como modificamos el contenido de la BD:
# python manage.py shell
# importabamos:
# from gestionPedidos.models import clientes
# creamos variable:
# cli = clientes(nombre = '', direccion = '', telefono='')
# cli.save()


# como hacer consultas:
# desde el shell
# python manage.py shell
# from gestionPedidos.models import articulos
# articulos.objects.filter(seccion= '')
# para consultar un rango:
# articulos.objects.filter(precio__range=[0, 200])
# para consultar mayor o menor que:
# articulos.objects.filter(precio__gte=60) ---- es equivalente a >
# articulos.objects.filter(precio__lte=60) ---- es equivalente a < 
# como pedir un orden (order by):
#  articulos.objects.filter(precio_gte=60).order_by('precio') ---- de menor a mayor
#  articulos.objects.filter(precio_gte=60).order_by('-precio') ---- de mayor a menor


# La informacion nos muestra en forma de Query, es decir en forma de tabla
# si yo quiero ver la informacion de una mejor manera:
# def __str__(self):
# transforma la informacion del objeto a string

# cada vez que hacemos una modificacion en models.py
# python manage.py makemigrations
# python manage.py migrate



# IMPORTANTE:
# panel de adminiatracion
# Es necesario por ejemplo eliminar usuario, agregar datos o modificarlos, sin usar codigo sql (es decir sin usar codigo)
# es necesario cuando la pagina web es compleja     
# es creado por defecto
# python manage.py runserver
# http://127.0.0.1:8000/admin/login/?next=/admin/
#para acceder al panel de administracion necesitamos usuario y contraseña
# necesitamos crear un superUsuario
# para configurar el panel de administracion
# EN LA CARPETA DEL PROYECTO
# python manage.py createsuperuser

# ---------------------------------------------

# PANEL DE ADMINISTRACION
# admin.py (vinculado a panel de administracion, en el cual no se va a haber ningun modelo hasta que se registre)
# codificar donde tenemos las tablas
# registrar los modelos (clientes, pedidos, articulos)
# hay que importar los modelos
# de esta forma vamos a ir agregando:

# from gestionPedidos.models import clientes, articulos, pedidos

# admin.site.register(clientes, clientesAdmin)
# admin.site.register(articulos, articulosAdmin)
# admin.site.register(pedidos, pedidosAdmin)

# en defecto los datos se van a negrita, es decir son campos requieridos no opcionales
# si quermos que sea opcional colocamos de argumento (blank= True, null=True)

# Si en panel queremos ver tablas o un determinado dato:
# en archivo admin.py
# crear una clase que herede de models.admin (nos permite realizar modificaciones en los modelos de administracion)
# Ademas de la clase hay que registrar esta nueva clase

# admin.site.register(clientes, clientesAdmin)

# class clientesAdmin(admin.ModelAdmin):
    # list_display = ('nombre', 'direccion', 'telefono')
    # si queremos poner un buscador --- search_fields = ('patron de busqueda')
    # search_fields= ('nombre', 'telefono')



# PARA CAMBIAR DE IDIOMA EL PANEL
# ir a settings.py en la parte de LENGUAGE_CODE = "en-us" hay que cambiar a "es-us"

# _______________________________________________________________________________
# crear formulario capaz de enviar la informacion al servidor:

# hay que crear un formulario en un archivo html creada de una carpeta template en el proyecto:
# la accion es que nos lleve a una direccion a otro html, el metodo utilizado GET (LA INFORMACION SE ENVIA)
# creamos el tipo de campo type = "text" y el tipo de informacion que el usuario introduce y para capturar esa información tenemos que identificarla name = "pdr"

# <form action="/buscar/" method="GET">
#     <input type="text" name="pdr">
#     <input type="submit" value="Buscar">
# </form>

# primero importamos las vistas, y debemos registrar en urls el html en modulo views.py y llamamos a la funcion ():


# from gestionPedidos import views
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('busqueda_productos/', views.busqueda_productos),
#     path('buscar/', views.buscar),


# ahora hay que decirle al servidor que registre (urls.py) esa url y tmb tenemos que crear una vista que nos lleve a ese formulario y despues nos lleve al url buscar

#  En carpeta views.py tenemos que crear las vistas que son funciones (def):
# necesitamos que nos renderice desde template(html) 

# def busqueda_productos(request):
#     return render(request, 'busquedas_productos.html')

# hay que pedirle al servidor que haga algo, a traves del Request (tiene metodos y propiedades) y el servidor puede manipular el request y puede obtener datos del usuario
# POR EJEMPLO EN VIEWS (Y DESPUES REGISTRAR EN URLS.PY)

# def busqueda_productos(request):
#     return render(request, 'busquedas_productos.html')

# def buscar(request):
#     # mensaje = f'Articulo buscado: {request.GET["pdr"]}'
    # return HttpResponse(mensaje)


# interaccion template (html) conlas vistas (views.py)
# cada vista (views.py) tenemos que asociarla a una urls (ursl.py) para poder dirigirnos al template (html)
# en las vistas vamos a poner funciones (def) que tomen o manden el dato del html (GET) con ese dato se hace una variable
# y se lo compara con lo que se encuentra en la base de datos (creando una variable de un objeto y en particular de un nombre por ejemplo)
# de estas dos variables se hace una nueva solicitud (render) y se lo envia a otro html
# este html va a tomar esta dos variables (una de la base de datos y otra proporcionada por el usuario en el html)



class clientes(models.Model):
    # CharField - para almacenar texto
    nombre = models.CharField(max_length=30)
    # si queremos modificar como se ve en la pantalla del panel de administracion sin que se modifique la tabla: verbose_name= 'elegir nombre'
    direccion = models.CharField(max_length=50, verbose_name='La Dirección')
    # EmailField - solo admite que sea un correo valido lo que se incorpora (@)
    # si queremos que un campo a rellenar sea solo opcional colocar (blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=10)
    def __str__(self):
        return f'nombre: {self.nombre}, direccion: {self.direccion}, email: {self.email}, telefono: {self.telefono}'



    
class articulos(models.Model):
    nombre= models.CharField(max_length= 30)
    seccion= models.CharField(max_length= 30)
    # IntegerField - se refiere a números enteros
    precio = models.IntegerField()

    def __str__(self):
        return f'El nombre es {self.nombre} la sección es {self.seccion} y el precio es {self.precio}' 



class pedidos(models.Model):
    numero = models.IntegerField()
    # DateField - solo dato fecha
    fecha = models.DateField()
    # BooleanField - si es verdadero o falso, es decir si se entrego  o no el pedido
    entregado = models.BooleanField()
    def __str__(self):
        return f'numero: {self.numero}, fecha: {self.fecha}, entregado: {"SI" if self.entregado else "NO"}'






# _--- base de datos de otro modelo para ir aprendiendo 

# En nuestra aplicación de preguntas, vamos a tener las siguientes cuatro views:

# Página índice – muestra las últimas preguntas.

# Detalle de pregunta – muestra el texto de la pregunta, sin resultados, junto con un form para votar.

# Página de resultados – muestra los resultados para una pregunta particular.

# Acción de votar – maneja el voto por una opción particular en una pregunta dada.

import datetime
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('fecha publicación')
    def __str__(self):
        return self.question_text
    # funcion para decir si fue publicado hace un día
    # se puede colocar que no coloque True o false sino solo con un simbolo mediante boolean = True
    # y con short_description modifiamos como se ve el campo
    def publicado_recientemente(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    publicado_recientemente.admin_order_field = 'pub_date'
    publicado_recientemente.boolean = True
    publicado_recientemente.short_description = 'Publicado Recientemente?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text



# Para llegar de una URL a una view, Django usa lo que se conoce como ‘URLconfs’. Un URLconf mapea patrones de URL (descriptos como expresiones regulares) a views.
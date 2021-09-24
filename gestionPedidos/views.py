from email.mime import multipart
from django import template
from django.http.response import HttpResponse
from django.shortcuts import render
from gestionPedidos.models import articulos
from gestionPedidos.forms import Formulario_contacto
from django.core.mail import send_mail
# Create your views here.

def busqueda_productos(request):
    return render(request, 'busquedas_productos.html')

def buscar(request):
    # mensaje = f'Articulo buscado: {request.GET["pdr"]}'
    # return HttpResponse(mensaje)
# -------------------------------------------------------------------

    # estamos pidiendo informacion que enviamos desde el cuadro de texto (pdr -- es el name del cuadro)
    # esto es para saber si la informacion llega al servidor
   if request.GET['pdr']:
       
        producto = request.GET["pdr"]

        if len(producto) > 10:
            mensaje = 'La busqueda tiene que contener menos de 10 caracteres'
            
        # incontains sustituye o es como like, nombre es lo que haya en producto
        # like nombre = 'str'
        else: 
            art = articulos.objects.filter(nombre__icontains = producto)
            #    redirigir Art a otro archivo html
            return render(request, "resultado_busqueda.html", {"Art" : art, "query": producto})
   else:
       mensaje = 'No has introducido nada'

   return HttpResponse(mensaje)

from TiendaOnline.settings import EMAIL_HOST_USER
from django.contrib import messages
from django.shortcuts import redirect, render, HttpResponse
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
from django.template.loader import get_template, render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def contacto(request):
    if request.method=='POST':
# para poner en variable la informacion que coloco el usuario
        # importamos el formulario de forms que toma el modelo
        miFormulario = Formulario_contacto(request.POST)

# si el formulario paso la validacion
# is_valid() nos indica si hay o no informacion dentro
# clueaned_data nos muestra la infomacion a traves de un diccionario
        if miFormulario.is_valid():
            infForm = miFormulario.cleaned_data

            # tambien podria ir Formulario_contacto(data= request.POST)
            # DATA es el paso de los datos que se recibiran



# de formulario podemos ir recuperando el valor colocando la clave
# para enviar la informacion lo hacemos a traves .get el segundo paramentro es el correo del servidor
            destinatario = request.POST['email']

            nombre = request.POST['nombre']
            mensaje = request.POST['mensaje']
            asunto = request.POST['asunto']
            

            # html = f"""
            # <html>
            # <body>
            # <p> Hola  {nombre} </p>
            # <p> nos pondremos en contacto con usted lo antes posible, le comunciamos que recibimos el siguiente mensaje: </p>
            # <p><b>{mensaje}</b></p>
            # <p>Atte. Andres Rodriguez </p>
            # </body>
            # </html>
            # """ 
            # mensaje = MIMEText(html, 'html')
            
            # msj = multipart("alternativa")
            # msj.attach(mensaje)

            # msj = f"Hola {nombre}, nos pondremos en contacto con usted lo antes posible, le comunciamos que recibimos el siguiente mensaje: \n\n {mensaje}. \n\n \t\t\t\t Atte.Andres Rodriguez"

            contexto = {'nombre': nombre, 'mensaje': mensaje}

            template = render_to_string('mensaje.html', contexto)
            
            # msj = get_template('mensaje.html')
            # content = msj.render(contexto)
            email = EmailMultiAlternatives(
                asunto,
                mensaje,
                settings.EMAIL_HOST_USER,
                [destinatario]
                
                )
            
            email.attach_alternative(template, 'text/html')
            email.send()

            
            # send_mail(infForm['asunto'], (email), infForm.get('email', ''), [destinatario],)

            #  (f"Hola {nombre}, nos pondremos en contacto con usted lo antes posible, le comunciamos que recibimos el siguiente mensaje: \n\n <b>{mensaje} </b>. \n\n \t\t\t\t Atte.Andres Rodriguez")


# otra variante
        # subject = request.POST['asunto']
        # message = request.POST['mensaje'] + ' ' + request.POST['email']
        # email_form = EMAIL_HOST_USER
        # recipent_list = ['rodrigueza.federacion@gmail.com']

        # send_mail = (subject, message, email_form, recipent_list)

            
            
            mensaje = messages.success(request, f'{nombre} has enviado un correo exitosamente')
# el return queda si o si
        return redirect('contacto')
        # return render(request, 'formulario_contacto.html', {'mensaje': mensaje})
        
    else:   
        # obtiene un formulario vacio
        miFormulario=Formulario_contacto()
        # seguidamente estmos pidiendo que debe renderizar a un html con el diccionario que encapsula la variable miFormulario
    return render(request, "formulario_contacto.html", {"form": miFormulario})
        # pedir que construya un html con los datos obtenidos



    #     subject = request.POST['asunto']
    #     message = request.POST['mensaje'] + ' ' + request.POST['email']
    #     email_form = settings.EMAIL_HOST_USER
    #     recipent_list = ['cursos@gmail.com']
    #     send_mail(subject, message, email_form, recipent_list)

    #     return render(request, "gracias.html")

    # return render(request, 'contacto.html')


# vistas basadas en clases
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import articulos

class CrearArticulo(CreateView):
    model = articulos
    fields = ['nombre', 'seccion', 'precio']
    template_name = "crear_articulos.html"
    
    
    







# vistas de la app pregutnas y votos


from gestionPedidos.models import Question, Choice
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.views import generic





#  intentando modificar las vistas basada en funciones, cambiarlas en vistas basadas en clases
"""
class index(generic.ListView):
    template_name = 'indice.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # Return the last five published questions.
        return Question.objects.order_by('-pub_date')[:5]

"""
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
    context = {
        'latest_question_list': latest_question_list,
    }
    # if latest_question_list:
    #     return redirect('detalle', context)

    # aca mandamos al contexto todas las Question (pregutnas) para sacar en el template el id para mandarlo a detail (Detalle_pregtuna.html)
    return render(request, 'indice.html', context)

"""
class detail(generic.DetailView):
    model = Question
    template_name = 'Detalle_Pregunta.html'


"""
def detail(request, question_id):
    
    # el id mandado por index es agarrado y nuevamente es identificado una pregunta (Question.id.question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'Detalle_Pregunta.html', {'question': question})
    

    # contexto = {'detalle': "You're looking at question %s." % question_id}
    # return render(request, 'Detalle_Pregunta.html', contexto)


"""
class results(generic.DetailView):
    model = Question
    template_name = 'Pagina_Resultados.html'

"""
def results(request, question_id):
    # contexto = {'response': "You're looking at the results of question %s.", 'question_id': question_id}
    # return render(request, 'Pagina_Resultados.html', contexto)
    
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'Pagina_Resultados.html', {'question': question})




def vote(request, question_id):
    # contexto = {'vota': "You're voting on question %s." % question_id}
    # return render(request, 'Votar.html', contexto)


    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'Detalle_Pregunta.html', {
            'question': p,
            'error_message': "No seleccionaste una opción",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('resultado', args=(p.id,)))



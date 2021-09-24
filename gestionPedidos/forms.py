# creacion de formularios a atraves de API FORMS
# configurar el mail backend en settings.py
# 
# EMAIL_BACKEND = "django.core.mail.backends.smtp.emailBackend"
# 
# EMAIL_HOST = "smtp.gmail.com" #HAY QUE ESPECIFICAR EL HOST: parametros de gmail en este caso, # tambien hay que configurar el gmial personal para poder usarlo para recibir correos
# deshabilitar Acceso de aplicaciones poco seguras, porque gmail viene por defecto la prohibición de terceros

# EMAIL_IUS_TSL = True #especificar protocolos para enviar el correo o parametros

# EMAIL_PORT = 587 #Es el puerto de gmail
# EMAIL_HOST_USSER = 'rodrigueza.federacion@gmail.com'
# EMAIL_HOST_PASSWORD = "Lgante03"

# libreria core.mail
from django import forms

# tenemos que crear una clase de ese formulario (de contacto)
# por crear esta clase 
#  con python manage.py shell
# podemos ingresar al shell
# from gestionPedidos.forms import Formulario_contacto
# podemos crear objetos (variables de las clases)
# MiFormulario = Formulario_contacto({'asunto': 'algo', 'email': 'maail@gmail.com', 'mensaje': 'este es mensaje de prueba'})
# colocamos MiFormulario.cleaned_data y se muestra en pantalla los datos
class Formulario_contacto(forms.Form):
    nombre = forms.CharField(label='nombre', required=True)
    asunto = forms.CharField(label='asunto', required=True)
    email = forms.EmailField(label='email', required=True)
    # con widget le damos la forma que queramos que tenga
    mensaje = forms.CharField(widget=forms.Textarea)


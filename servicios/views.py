from django.shortcuts import render

# Create your views here.

# hay que registrar la url de busqueda para que los archivos jpg puedan verse

# hay que importar la clase del app servicio
from servicios.models import servicios

def Servicios(request):
    # importar todos los servicios u objetos creados en el modulo servicios
    servicio = servicios.objects.all()
    return render(request, "servicios/servicios.html", {'servicio': servicio})






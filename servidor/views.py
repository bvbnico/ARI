from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

from django.http import HttpResponseNotFound
from .models import *
# Create your views here.



def index(request):

    #Función vista para la página inicio del sitio.
    # Genera contadores de algunos de los objetos principales
    #num_estaciones= request.GET.get('cliente_id')
    num_estaciones= estaciones.objects.filter(estacion_id=1)
    num_clientes=clientes.objects.filter(estacion_id=1)
    # Libros disponibles (status = 'a')
    num_tipo_sensor=tipo_sensor.objects.all()
    num_sensores=sensores.objects.count()  # El 'all()' esta implícito por defecto.

        # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_estaciones':num_estaciones,'num_clientes':num_clientes,'num_tipo_sensor':num_tipo_sensor,'num_sensores':num_sensores},)


@csrf_exempt
def devices_posts(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        id_sensor = body['id_sensor']
        #print(body,int(id_sensor))
        alarmas.objects.create(sensor_id=id_sensor, estado="Pendiente")
    return JsonResponse("success")
   

def users_view(request):
    if request.method == 'GET':
        c = clientes.objects.all()
        return render(request, 'general.html', {'clientes': c})
    return HttpResponseNotFound("")
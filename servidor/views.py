from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json

from django.http import HttpResponse
from .models import estaciones, clientes, sensores, tipo_sensor, usuarios

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
def post_list(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    id_station = body['id_station']
    id_client = body['id_client']
    id_sensor = body['id_sensor']
    print(body,int(id_station))
    return JsonResponse(body)
    #c = {'recibido':"0"}
    """if request.method == 'POST':
        #'[true,false,{"SensorType":"Temperature":"values"}]'
        #data = request.POST
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        id_station = body['id_station']
        id_client = body['id_client']
        id_sensor = body['id_sensor']
        print(body,id_station)
        c = {'recibido':"0"}"""

    #print(body,id_station)
    estacion= estaciones.objects.filter(estacion_id=int(id_station))
    cliente=clientes.objects.filter(cliente_id=int(id_client))
    # Libros disponibles (status = 'a')
    num_tipo_sensor=tipo_sensor.objects.all()
    num_sensores=sensores.objects.count()  # El 'all()' esta implícito por defecto.
    return render(
        request,
        'index.html',
        context={'estacion':estacion,'cliente':cliente,'num_tipo_sensor':num_tipo_sensor,'num_sensores':num_sensores},)

    #return JsonResponse(c)


"""
from django.views import generic

class inicio(generic.ListView):
    model = clientes

class BookDetailView(generic.DetailView):
        model = Book"""

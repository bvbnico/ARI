from django.shortcuts import render, get_object_or_404, redirect,render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from django.http import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth import models
from django.http import HttpResponseNotFound
from .models import *
# Create your views here.



def index(request):

    #Función vista para la página inicio del sitio.
    # Genera contadores de algunos de los objetos principales
    #num_estaciones= request.GET.get('cliente_id')
    #num_estaciones= estaciones.objects.filter(i=1)
    num_clientes=clientes.objects.filter(id_cliente=1)
    # Libros disponibles (status = 'a')
    num_tipo_sensor=tipo_sensor.objects.all()
    num_sensores=sensores.objects.count()  # El 'all()' esta implícito por defecto.
    #poner a estado de espera como un boton
    c = clientes.objects.filter(id_cliente=1).update(estado="espera")

        # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={"""'num_estaciones':num_estaciones,"""'num_clientes':num_clientes,'num_tipo_sensor':num_tipo_sensor,'num_sensores':num_sensores},)

def login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user.is_superuser:
            return HttpResponseRedirect('/home/general/')
    return render(request,'login.html')

@csrf_exempt
def devices_posts(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        id_sensor = body['id_sensor']
        id_client = body['id_client']
        c = clientes.objects.filter(id_cliente = id_client).update(estado="pendiente")
        c = clientes.objects.filter(estado="pendiente")
        #print(body,int(id_sensor))
        d = {'recibido':"0"}
    return JsonResponse(d)


def users_view(request):
    if request.method == 'GET':
        #c = clientes.objects.all()
        a = 2
        #c = clientes.objects.filter(id_cliente = a).update(estado="pendiente")
        #c = clientes.objects.filter(estado="pendiente").values('nombre')
        #esto va a ser ùtil para guardar los registros estadìsticos en otros modelos
        c = clientes.objects.filter(estado="pendiente")
        #c = clientes.objects.values('nombre')
        
        return render(request, 'general.html', {'clientes': c})
    return HttpResponseNotFound("")

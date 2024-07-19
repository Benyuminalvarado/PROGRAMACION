from django.shortcuts import render, redirect, get_object_or_404
from .models import Autos, Carrito
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login



def home(request):
    autos_list = Autos.objects.all()
    return render(request, 'core/index.html')

def login(request):
    return render(request, 'core/login.html')

def index_vehiculo(request):
    autos = Autos.objects.all()
    return render(request, 'core/index_vehiculos.html', {'autos': autos})

def cotizaciones(request):
    return render(request, 'core/index_cotizaciones.html')

def personal(request):
    return render(request, 'core/personal.html')

def servicio(request):
    return render(request, 'core/servicio.html')

def fotos(request):
    return render(request, 'core/fotos.html')

@login_required
def carrito(request):
    carrito_items = Carrito.objects.filter(usuario=request.user)
    total = sum(item.auto.precio * item.cantidad for item in carrito_items)
    return render(request, 'core/carrito.html', {'carrito': carrito_items, 'total': total})

@login_required
def agregar_al_carrito(request, auto_id):
    auto = get_object_or_404(Autos, id=auto_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user, auto=auto)
    if not created:
        carrito.cantidad += 1
        carrito.save()
    return redirect('carrito')

@login_required
def eliminar_del_carrito(request, auto_id):
    auto = get_object_or_404(Autos, id=auto_id)
    carrito = Carrito.objects.get(usuario=request.user, auto=auto)
    carrito.delete()
    return redirect('carrito')


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home') 
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'core/login.html')


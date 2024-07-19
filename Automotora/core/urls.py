
from django.urls import path
from . import views  
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('login/', views.custom_login, name="login"),
    path('vehiculo/', views.index_vehiculo, name="vehiculo"),
    path('cotizaciones/', views.cotizaciones, name="cotizaciones"),
    path('personal/', views.personal, name="personal"),
    path('servicio/', views.servicio, name="servicio"),
    path('fotos/', views.fotos, name="fotos"),
    path('carrito/', views.carrito, name='carrito'),
    path('agregar/<int:auto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/eliminar/<int:auto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
]

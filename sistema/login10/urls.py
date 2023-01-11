from django.urls import path
from . import views

# ? urls

urlpatterns = [
    path('', views.home, name='home'),
    #! Autenticated BLOCK
    path('registrate/', views.registrate, name='registrate'),
    path('iniciar/sesion/',views.iniciar_sesion,name='iniciarsesion'),
    path('cerrar/sesion',views.cerrar_sesion, name='cerrarsesion'),
    
    
    #! 
    path('agregar/empleado/', views.agregar_empleado, name='agregar_empleado'),
    path('eliminar/<id>',views.eliminar_empleado),
]


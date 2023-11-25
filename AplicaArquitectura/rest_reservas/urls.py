from django.urls import path
from rest_reservas.views import lista_reserva ,lista_doctores ,lista_departamentos

urlpatterns=[
 path('',lista_reserva, name='lista_reserva'),
 path('reserva',lista_reserva, name='lista_reserva'),
 path('doctores',lista_doctores, name='lista_doctores'),
 path('departamentos',lista_departamentos, name='lista_departamentos'),
]
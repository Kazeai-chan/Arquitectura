from django.urls import path
from rest_reservas.views import lista_reserva

urlpatterns=[
 path('',lista_reserva, name='lista_reserva'),
 path('lista_reserva',lista_reserva, name='lista_reserva'),
]
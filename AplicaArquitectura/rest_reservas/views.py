from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from GlobalMed.models import reserva ,doctores ,departamentos
from .serializers import ReservaSerializer
@csrf_exempt
@api_view(['GET'])

def lista_reserva(request):
    """
    LISTA TODOS LOS USUARIOS
    """
    if request.method == 'GET':
        reservas = reserva.objects.all()
        #print(reservas)
        # doctor = doctores.objects.all()
        # depto = departamentos.objects.all()
        serializer = ReservaSerializer(reservas, many=True)
    return Response(serializer.data)



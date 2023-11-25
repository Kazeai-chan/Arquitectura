from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from GlobalMed.models import reserva ,doctores ,departamentos
from .serializers import ReservaSerializer ,DepartamentosSerializer ,DoctoresSerializer
@csrf_exempt
@api_view(['GET'])

def lista_reserva(request):
    """
    """
    if request.method == 'GET':
        reservas = reserva.objects.all()
        #print(reservas)
        # doctor = doctores.objects.all()
        # depto = departamentos.objects.all()
        serializer = ReservaSerializer(reservas, many=True)
    return Response(serializer.data)

@csrf_exempt
@api_view(['GET'])
def lista_doctores(request):
    """
    """
    if request.method == 'GET':
        doctor = doctores.objects.all()
        serializer = DoctoresSerializer(doctor, many=True)
    return Response(serializer.data)

@csrf_exempt
@api_view(['GET'])

def lista_departamentos(request):
    """
    """
    if request.method == 'GET':
        departamento = departamentos.objects.all()
        serializer = DepartamentosSerializer(departamento, many=True)
    return Response(serializer.data)
from rest_framework import serializers
from GlobalMed.models import reserva ,departamentos, doctores

class ReservaSerializer(serializers.ModelSerializer):
    nombre_dep = departamentos.nombre_dep
    nombre = doctores.nombre
    class Meta:
        model = reserva
        fields = [
            'idreserva',
            'nombre',
            'correo',
            'fecha',
            'hora',
            'comentario',
            'doctor',
            'departamento']
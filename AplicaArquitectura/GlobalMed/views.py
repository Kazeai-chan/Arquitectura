from django.shortcuts import render
from .models import reserva
from .models import doctores
from .models import departamentos
from .forms import reservaForm
from django.views.generic.list import ListView
from django.views import generic
from django.http import JsonResponse

# Create your views here.
# def home(request):
#     return render(request,'globalmed/index.html')

def home(request):
    doctor = doctores.objects.all()
    departamento = departamentos.objects.all()
    datos = {
        'form' : reservaForm(),
        'doctor' : doctor,
        'departamento' : departamento,
    }
    if request.method=='POST':

        #para definir el tipo de envío
        formulario = reservaForm(request.POST)
        
        # for field in formulario:
        #     print("Field Error:", field.name ,field.errors)

        if formulario.is_valid():
            #departamento = departamentos.objects.get(nombre_dep=nomDep).id
            
            formulario.save()
            datos['mensaje'] = "Guardados correctamente"
        else:
            datos['mensaje'] = ("falló guardado ")
            
    return render(request,'globalmed/index.html',datos)

def listaDoc(request):
    #doctor = doctores.objects.all()
    result_list = list(doctores.objects.all()\
                .values('id', 
                        'nombre',
                        'id_dep',
                       ))
    return JsonResponse(result_list, safe=False)

def listaRes(request,id_doc,fechaR):

    result_list = list(reserva.objects.all().filter(doctor=id_doc,fecha=fechaR)\
                .values('doctor', 
                        'fecha',
                        'hora',
                       ))
    
    return JsonResponse(result_list, safe=False)

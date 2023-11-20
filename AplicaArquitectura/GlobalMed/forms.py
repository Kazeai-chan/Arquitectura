from dataclasses import field
# from django.views.generic.list import ListView
from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import reserva
from .models import departamentos
#from .views import listaDeps
from django.views import generic





class DateInput(forms.DateInput):
    input_type = 'date'


class reservaForm(ModelForm):
    class Meta:
        model = reserva
        fields = ['nombre','correo','fecha',
        'hora','departamento','doctor','comentario']


        widgets = {
            #'hora': forms.Select(choices=horas),
            'fecha': DateInput(),
            'comentario':forms.Textarea(),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class':'form-control','required':'','type':'txt','id':'name', 'placeholder':'Su Nombre', 'data-rule':'minlen:4', 'data-msg':'Por favor elija a lo menos 4 carácteres'})
        self.fields['correo'].widget.attrs.update({'class': 'form-control','required':'','type':'email','id':'email','placeholder':'Su Email', 'data-rule':'email', 'data-msg':'Ingrese un correo válido'})
        self.fields['fecha'].widget.attrs.update({'class': 'form-control','required':'','type':'date','id':'date','min':'Date()','onchange':'limpiaFecha()'})
        self.fields['comentario'].widget.attrs.update({'class':'form-control','type':'txt','id':'message','rows':'5', 'placeholder':'Mensaje (Opcional)'})


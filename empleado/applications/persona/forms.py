from django import forms
from django.db.models import fields
from django.forms import widgets

from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    """EmpleadoForm definition."""
    
    class Meta:
        model = Empleado
        fields = (
            'first_name',
            'last_name',
            'job',
            'departamento',
            'image',
            'habilidades',
        )

        widgets = {
            'habilidades': forms.CheckboxSelectMultiple(
                
            )
        }

from django import forms
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from applications.persona import models

from applications.persona.models import Empleado
from .models import Departamento
from .forms import NewDepartamentoForm

class DepartamentoListView(ListView):
    template_name = "departamento/lista.html"
    model = Departamento
    context_object_name = "departamentos"

class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        depa = Departamento(
            name = form.cleaned_data['departamento'],
            shor_name = form.cleaned_data['shorname']
        )
        depa.save()

        nombre  = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellidos,
            job = '1',
            departamento = depa
        )

        return super(NewDepartamentoView, self).form_valid(form)

# Create your views here.

from django.forms import forms
from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    TemplateView, 
    ListView,
    CreateView
)

from .models import Prueba

from .forms import PruebaForm

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'

class ResumenFundationView(TemplateView):
    template_name = 'home/resumen_fundation.html'

class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'listaNumeros'
    queryset = ['0','1','10','20','30']


class PruebaListView(ListView):
    model = Prueba
    template_name = "home/lista_prueba.html"
    context_object_name = 'lista'


class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    # fields = ['titulo','subtitulo','cantidad']
    form_class = PruebaForm
    success_url = '/'
from django.db.models.fields import files
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (     
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)
# Create your views here.

from .models import Empleado
from .forms import EmpleadoForm

class InicioView(TemplateView):
    template_name = "inicio.html"

class listAllEmpleados(ListView):
    template_name = 'persona/lista_all.html'
    paginate_by = 4
    ordering = "first_name"
    # model = Empleado
    # context_object_name = 'lista'

    
    def get_queryset(self):       
        palabra_clave = self.request.GET.get('kword','')
        lista = Empleado.objects.filter(
            full_name__icontains = palabra_clave
        )
        return lista


class listByAreaEmpleados(ListView):
    template_name = "persona/lista_by_area.html"
    context_object_name = "empleados"

    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__name = area
        )
        return lista

        
class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = "id"
    # model = Empleado
    context_object_name = 'empleados'
    model = Empleado


class ListEmpleadosByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):       
        palabra_clave = self.request.GET.get('kword','')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        return lista

class ListaHabilidadesEmpleado(ListView):
    template_name = 'persona/habiliades.html'
    context_object_name = 'habiliadades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id = 15)
        return empleado.habilidades.all()
    
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona\detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context
        

class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    # fields = [
    #     'first_name',
    #     'last_name', 
    #     'job',
    #     'departamento',
    #     'habilidades',
    #     'image',
    # ]
    form_class = EmpleadoForm
    # fields = ('__all__')
    success_url = reverse_lazy('persona_app:correcto') 

    def form_valid(self, form):
        empleado = form.save()
        empleado.full_name = empleado.first_name = ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields = [
        'first_name',
        'last_name', 
        'job',
        'departamento',
        'habilidades',
    ]
    # success_url = reverse_lazy('persona_app:correcto') 
    success_url = reverse_lazy('persona_app:empleados_admin') 

    def post(self, request, *args, **kwargs) :
        self.object = self.get_object()
        # print(request.POST)
        # print(request.POST['first_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super(EmpleadoUpdateView, self).form_valid(form)



class EmpleadoDeleteView(DeleteView):
    template_name = "persona/delete.html"
    model = Empleado
    # success_url = reverse_lazy('persona_app:correcto') 
    success_url = reverse_lazy('persona_app:empleados_admin') 

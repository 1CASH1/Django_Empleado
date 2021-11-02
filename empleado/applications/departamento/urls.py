from django.contrib import admin
from django.urls import path

from . import views

# def DesdeApps(self):
#     print('=========HOLA LA APP DEPARTAMENTOS=========')

app_name = "departamento_app"

urlpatterns = [
    # path('departamento/', DesdeApps),
    path(
        'departamento-list/', 
        views.DepartamentoListView.as_view(),
        name='departamento_list'
    ),
    path('new-departamento/', views.NewDepartamentoView.as_view(),name='nuevo_departamento')
]

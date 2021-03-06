from django.contrib import admin
from .models import Empleado, Habiliades
# Register your models here.

admin.site.register(Habiliades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
        'id',
    )
    #
    def full_name(self, obj):
        #toda la operacion
        #print(obj)
        return obj.first_name + ' ' + obj.last_name
    #
    search_fields = ('first_name',)
    list_filter = ('departamento','job','habilidades',)
    #
    filter_horizontal = ('habilidades',)
admin.site.register(Empleado,EmpleadoAdmin)
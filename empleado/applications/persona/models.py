from django.db import models
from django.db.models.base import Model
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

class Habiliades(models.Model):
    Habilidad = models.CharField('Habilidad',max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'

    def __str__(self):
        return  str(self.id) + '-' + self.Habilidad 
    

# Create your models here.
class Empleado(models.Model):
    """ Modelo para tabla empleados"""
    JOB_CHOICES = (
        ('0','CONTADOR'),
        ('1','ADMINISTRADOR'),
        ('2','ECONOMISTA'),
        ('3','OTRO'),
    )
    first_name = models.CharField('Nombres', max_length=50)
    last_name = models.CharField('Apellido', max_length=50)
    full_name = models.CharField(
        'Nombre Completo', 
        max_length=50,
        blank=True
    )
    job = models.CharField('Trabajo', max_length=1,choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    image = models.ImageField( upload_to='empleado', height_field=None, width_field=None, max_length=None, blank=True)
    habilidades = models.ManyToManyField(Habiliades)

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name
    

from django.db import models
from .Empleado import Empleado

class Cliente (models.Model):
    cli_id        = models.AutoField(primary_key = True)
    cli_nombre    = models.CharField('Nombre', max_length = 30)
    cli_apellido  = models.CharField('Apellido', max_length = 30)
    cli_celular   = models.CharField('Celular', max_length = 15)
    cli_direccion = models.CharField('Direccion', max_length = 30)
    cli_recomendaciones = models.TextField('Recomendaciones')
    #empleado_fk_id = models.ForeignKey(Empleado, related_name = 'EmpleadoCliente', on_delete = models.CASCADE)
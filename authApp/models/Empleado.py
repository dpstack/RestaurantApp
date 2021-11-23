from django.db import models

class Empleado(models.Model):
    emp_cedula   = models.IntegerField(primary_key=True)
    emp_nombre   = models.CharField('Nombre', max_length = 30)
    emp_apellido = models.CharField('Apellido', max_length = 30)
    emp_celular  = models.CharField('Celular', max_length = 15)
    emp_correo   = models.CharField('Correo', max_length = 30)
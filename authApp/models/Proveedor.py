from django.db import models

class Proveedor(models.Model):
    prov_nit       = models.IntegerField(primary_key = True)
    prov_nombre    = models.CharField('Nombre', max_length = 30)
    prov_celular   = models.CharField('Celular', max_length = 15)
    prov_direccion = models.CharField('Dirección', max_length = 30)
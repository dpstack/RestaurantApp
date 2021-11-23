from  django.db  import models
""" from .Cliente    import Cliente
from .Proveedor  import Proveedor """

class Producto(models.Model):
    prod_id       = models.AutoField(primary_key=True)
    prod_nombre   = models.CharField('Nombre', max_length = 45)
    prod_precio   = models.IntegerField()
    prod_cantidad = models.IntegerField()
    prod_tipo     = models.CharField('Tipo', max_length = 45)
    # cliente_fk    = models.ForeignKey(Cliente,   related_name = 'ClienteProducto',   on_delete = models.CASCADE)
    #proveedor_fk  = models.ForeignKey(Proveedor, related_name = 'ProveedorProveedor', on_delete = models.CASCADE)
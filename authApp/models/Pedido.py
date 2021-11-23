from django.db  import models
from .Empleado  import Empleado
from .Cliente   import Cliente
from .Proveedor import Proveedor
from .Producto  import Producto

class Pedido(models.Model):
    ped_id    = models.IntegerField(primary_key   = True)
    ped_fecha = models.DateTimeField(auto_now_add = True)
    ped_emp_cedula = models.ForeignKey(Empleado,  related_name = 'Empleado',  on_delete = models.CASCADE)
    cliente_cli_id      = models.ForeignKey(Cliente,   related_name = 'Cliente',   on_delete = models.CASCADE)
    proveedor_prov_nit  = models.ForeignKey(Proveedor, related_name = 'ProveedorPedido', on_delete = models.CASCADE)
    producto_prod_id    = models.ForeignKey(Producto,  related_name = 'ProductoPedido',  on_delete = models.CASCADE)

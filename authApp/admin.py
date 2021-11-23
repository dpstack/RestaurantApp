from django.contrib import admin

from .models.Admin     import Admin
from .models.Empleado  import Empleado
from .models.Cliente   import Cliente
from .models.Proveedor import Proveedor
from .models.Producto  import Producto
from .models.Pedido    import Pedido

admin.site.register(Admin)
admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Pedido)

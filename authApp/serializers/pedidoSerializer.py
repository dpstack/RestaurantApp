from rest_framework import serializers
from authApp.models.Pedido    import Pedido
from authApp.models.Cliente   import Cliente
from authApp.models.Empleado  import Empleado
from authApp.models.Producto  import Producto
from authApp.models.Proveedor import Proveedor
from authApp.serializers.clienteSerializer import ClienteSerializer
from authApp.serializers.empleadoSerializer import EmpleadoSerializer
from authApp.serializers.productoSerializer import ProductoSerializer
from authApp.serializers.proveedorSerializer import ProveedorSerializer

class PedidoSerializer (serializers.ModelSerializer):

    cliente   = ClienteSerializer()
    empleado  = EmpleadoSerializer()
    producto  = ProductoSerializer()
    proveedor = ProveedorSerializer()

    class Meta: 

        model  = Pedido
        fields = ['ped_fecha', 'empleado', 'cliente', 'proveedor', 'producto']

        def to_representation (self, obj):

            pedido    = Pedido.objects.get(ped_id = obj.ped_id)
            cliente   = Cliente.objects.get(cli_id = obj.cli_id)
            empleado  = Empleado.objects.get(emp_id = obj.emp_id)
            producto  = Producto.objects.get(prod_id = obj.prod_id)
            proveedor = Proveedor.objects.get(prov_id = obj.prov_id)

            return {

                'id_pedido' : pedido.ped_id,
                'fecha'     : pedido.ped_fecha,
                'cliente'   : {

                    'nombre'   : cliente.cli_nombre,
                    'apellido' : cliente.cli_apellido,
                    'celular'  : cliente.cli_celular,
                    'direccion'       : cliente.cli_direccion,
                    'recomendaciones' : cliente.cli_recomendaciones,

                },
                'empleado' : {

                    'cedula'   : empleado.emp_cedula,
                    'nombre'   : empleado.emp_nombre,
                    'apellido' : empleado.emp_apellido,

                },
                'producto' : {

                    'nombre'   : producto.prod_nombre,
                    'precio'   : producto.prod_precio,
                    'cantidad' : producto.prod_cantidad,
                    'tipo'     : producto.prod_tipo,

                },
                'proveedor' : {

                    'nombre' : proveedor.prov_nombre,

                }


            }
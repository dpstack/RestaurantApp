from rest_framework          import serializers
from authApp.models.Producto import Producto
#from authApp.models.Cliente  import Cliente
#from authApp.models.Proveedor  import Proveedor
#from authApp.serializers.clienteSerializer import ClienteSerializer
#from authApp.serializers.proveedorSerializer import ProveedorSerializer

class ProductoSerializer (serializers.ModelSerializer):

    #cliente   = ClienteSerializer()
    #proveedor = ProveedorSerializer() 

    class Meta:

        model  = Producto
        fields = ['prod_nombre', 'prod_precio', 'prod_cantidad', 'prod_tipo'] 

        """ def to_representation (self, obj): 

            producto  = Producto.objects.get(prod_id = obj.prod_id)
            #cliente   = Cliente.objects.get(cli_id = obj.cli_id)
            proveedor = Proveedor.objects.get(prov_id = obj.prov_id)

            return {

                'prod_nombre'   : producto.prod_nombre,
                'prod_precio'   : producto.prod_precio,
                'prod_cantidad' : producto.prod_cantidad,
                'prod_tipo'     : producto.prod_tipo, 
                 'cliente'       : {

                    'nombre'   : cliente.cli_nombre,
                    'apellido' : cliente.cli_apellido,
                    'celular'  : cliente.cli_celular,
                    'direccion'       : cliente.cli_direccion,
                    'recomendaciones' : cliente.cli_recomendaciones,

                },
                'proveedor' : {

                    'nombre' : proveedor.prov_nombre,

                }

            } """
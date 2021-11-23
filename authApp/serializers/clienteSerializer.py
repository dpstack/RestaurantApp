from rest_framework         import serializers
from authApp.models.Cliente import Cliente

class ClienteSerializer (serializers.ModelSerializer):

    class Meta:

        model  = Cliente
        fields = ['cli_nombre', 'cli_apellido', 'cli_celular', 'cli_direccion', 'cli_recomendaciones'] 
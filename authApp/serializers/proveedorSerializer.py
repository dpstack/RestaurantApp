from rest_framework           import serializers
from authApp.models.Proveedor import Proveedor

class ProveedorSerializer (serializers.ModelSerializer):

    class Meta:

        model  = Proveedor
        fields = ['prov_nit', 'prov_nombre'] 
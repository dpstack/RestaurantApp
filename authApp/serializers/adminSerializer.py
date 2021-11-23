from rest_framework       import serializers
from authApp.models.Admin import Admin

class AdminSerializer (serializers.ModelSerializer):
    class Meta:

        model  = Admin
        fields = ['admin_id', 'username', 'password'] 

        def create (self, validated_data):

            adminInstance = Admin.objects.create(**validated_data)
            return adminInstance

        def to_representation (self, obj):

            admin = Admin.objects.get(admin = obj.admin_id)

            return {

                'admin_id'   : admin.admin_id,
                'Usuario'    : admin.username,
                'Contraseña' : admin.password,

            }
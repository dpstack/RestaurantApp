from rest_framework          import serializers
from authApp.models.Empleado import Empleado

class EmpleadoSerializer (serializers.ModelSerializer):

    class Meta:

        model  = Empleado
        fields = ['emp_cedula', 'emp_nombre', 'emp_apellido'] 
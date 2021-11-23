from authApp.models import Empleado
from authApp.serializers import EmpleadoSerializer
from rest_framework import generics


class EmpleadoList(generics.ListCreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer


class EmpleadoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

""" from authApp.models import Empleado
from authApp.serializers import EmpleadoSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class EmpleadoList (APIView):

    def get (self, request, format = None):

        empleados  = Empleado.objects.all()
        serializer = EmpleadoSerializer(empleados, many = True) 
        return Response(serializer.data)
    
    def post (self, request, format = None):

        serializer = EmpleadoSerializer(data = request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class EmpleadoDetail (APIView):

    def get_object(self, pk):

        try:
            return Empleado.objects.get(pk = pk)
        except Empleado.DoesNotExist:
            raise Http404
    
    def get (self, request, pk, format = None):

        empleados  = self.get_object(pk)
        serializer = EmpleadoSerializer(empleados)
        return Response(serializer.data)
    
    def put (self, request, pk, format = None):

        empleado = self.get_object(pk)
        serializer = EmpleadoSerializer(empleado, data = request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def delete (self, request, pk, format = None):

        empleados  = self.get_object(pk)
        empleados.delete()
        return Response(status = status.HTTP_204_NO_CONTENT) """
from authApp.models import Producto
from authApp.serializers import ProductoSerializer
from rest_framework import generics


class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer



"""from authApp.models import Producto
from authApp.serializers import ProductoSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ProductsList (APIView):

    def get (self, request, format = None):

        productos  = Producto.objects.all()
        serializer = ProductoSerializer(productos, many = True)
        return Response(serializer.data)

    def post (self, request, format = None):

        serializer = ProductoSerializer(data = request.data)
        
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ProductsDetail (APIView):

    def get_object (self, pk):

        try:
            return Producto.objects.get(pk = pk)
        except Producto.DoesNotExist:
            raise Http404

    def get (self, request, pk, format = None):

        producto   = self.get_object(pk)
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)

    def put (self, request, pk, format = None):

        producto   = self.get_object(pk)
        serializer = ProductoSerializer(producto, data = request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete (self, request, pk, format = None):

        producto = self.get_object(pk)
        producto.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        """
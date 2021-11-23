"""authProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from authApp import views
from authApp.views import productCreateView
from authApp.views import empleadoCreateView
from authApp.views import pedidoCreateView
from authApp.views import clienteCreateView
from authApp.views import proveedorCreateView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('products/', productCreateView.ProductoList.as_view()),
    path('products/<int:pk>', productCreateView.ProductoDetail.as_view()),
    path('empleados/', empleadoCreateView.EmpleadoList.as_view()),
    path('empleados/<int:pk>', empleadoCreateView.EmpleadoDetail.as_view()),
    path('proveedor/', proveedorCreateView.ProveedorList.as_view()),
    path('proveedor/<int:pk>', proveedorCreateView.ProveedorDetail.as_view()),
    path('cliente/', clienteCreateView.ClienteList.as_view()),
    path('cliente/<int:pk>', clienteCreateView.ClienteDetail.as_view()),
    path('pedido/', pedidoCreateView.PedidoList.as_view()),
    path('pedido/<int:pk>', pedidoCreateView.PedidoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from ApiProductos.models import Productos
from ApiProductos.serializers import ProductosSerializer
from rest_framework.decorators import api_view
from rest_framework import status
#from django.shortcuts import render, HttpResponse, redirect

##########################
##METODOS PARA PRODUCTOS##
##########################

#Consultar productos
@api_view(['GET', 'POST'])
def MetProductos(request):

    if request.method == 'GET':
        Prod=Productos.objects.all()
        serializer=ProductosSerializer(Prod,many=True)
        return JsonResponse(serializer.data,safe=False)

#Guardar productos
    elif request.method == 'POST':  
        serializer = ProductosSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#buscar, actualizar, eliminar productos, se hace por el id del producto
@api_view(['GET', 'PUT', 'DELETE'])
def productos_detail(request,key):
    try:
        prod = Productos.objects.get(pk=key)
    except Productos.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductosSerializer(prod)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductosSerializer(prod, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        prod.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

#consulta de productos por nombre
@api_view(['GET'])
def producto_nombre(request,nom):
    try:
        prod = Productos.objects.get(name=nom)
    except Productos.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductosSerializer(prod)
        return JsonResponse(serializer.data)

#consulta de productos por precio
@api_view(['GET'])
def producto_precio(request,pre):
    try:
        prod = Productos.objects.get(price=pre)
    except Productos.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductosSerializer(prod)
        return JsonResponse(serializer.data)
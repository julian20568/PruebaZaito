from rest_framework import serializers
from ApiProductos.models import Productos

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Productos
        fields=['cod','name','stock','price','paused']
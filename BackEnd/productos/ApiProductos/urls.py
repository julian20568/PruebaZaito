from django.urls import path
from ApiProductos import views

urlpatterns=[
    ###############################
    #RUTAS PARA LA CLASE PRODUCTOS#
    ###############################
    path('productos',views.MetProductos),
    path('productos/<int:key>',views.productos_detail),
    path('productos/nombre/<str:nom>', views.producto_nombre),
    path('productos/precio/<str:pre>', views.producto_precio),
]
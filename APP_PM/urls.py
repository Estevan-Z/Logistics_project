from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('editar-producto/<str:producto_id>/', views.editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:id_producto>/', views.eliminar_producto, name='eliminar_producto'),
    path('producto/<str:producto_id>/', views.productos_creados, name='productos_creados'),
    path('productos_listado/', views.productos_listado, name='productos_listado'),
    
    path('agregar_nota_entrada/', views.agregar_nota_entrada, name='agregar_nota_entrada'),
    path('buscar_producto/', views.buscar_producto, name='buscar_producto'),
    path('insertar-productos/', views.insertar_productos, name='insertar_productos'),

    path("generar_pdf/", views.generar_pdf, name="generar_pdf"),
    path('lista_proveedores/', views.lista_proveedores, name='lista_proveedores'),
    path('crear_proveedor/', views.crear_proveedor, name='crear_proveedor'),

    path('buscar_proveedor/', views.buscar_proveedor, name='buscar_proveedor'),

]

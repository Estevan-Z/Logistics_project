
from django.db import models
import random
import string
class Crear_producto(models.Model):
    LINEA_OPCIONES = [
        ('001', 'Fertilizantes'),
        ('002', 'Bioinsumos'),
        ('003', 'Materia Prima'),
        ('004', 'Coayudantes'),
        ('005', 'Comercializacion de productos'),
        ('006', 'Equipos de pulverizador'),
        ('007', 'Fungicidas'),
        ('008', 'Herbicidas'),
        ('009', 'Insecticidas'),
        ('010', 'Insumos'),
        ('011', 'Mercancia en Consignacion'),
        ('012', 'Productos fabricados - No Propios'),
    ]

    GRUPO_OPCIONES = [
        ('001', 'Biofungicidas'),
        ('002', 'Comercializacion de productos'),
        ('003', 'Materia Prima'),
        ('004', 'Fertilizantes'),
        ('005', 'Foliares'),
        ('006', 'Granulados'),
        ('007', 'Insumos'),
        ('008', 'Liquido'),
        ('009', 'Organicos'),
        ('010', 'Polvo'),
        ('011', 'Productos fabricados - No Propios'),
        ('012', 'Pulverizador Liquido'),
    ]
    
    id_producto = models.CharField(max_length=10, unique=True, editable=False, blank=True)
    nombre_producto = models.CharField(max_length=100)
    linea = models.CharField(max_length=100, choices=LINEA_OPCIONES)  
    grupo = models.CharField(max_length=100, choices=GRUPO_OPCIONES)
    marca = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_producto

    def save(self, *args, **kwargs):
        if not self.id_producto:
            self.id_producto = ''.join(random.choices(string.digits, k=10))
            while Crear_producto.objects.filter(id_producto=self.id_producto).exists():
                self.id_producto = ''.join(random.choices(string.digits, k=10))
        super(Crear_producto, self).save(*args, **kwargs)

#INSERTAR PRODUCTOS
class InsertarProductos(models.Model):
    archivo = models.FileField(upload_to='uploads/', verbose_name="Archivo Excel")
    fecha_subida = models.DateTimeField(auto_now_add=True)
    procesado = models.BooleanField(default=False, verbose_name="¿Procesado?")

    def __str__(self):
        return f"Archivo {self.archivo.name} - {'Procesado' if self.procesado else 'Pendiente'}"

class NotaEntrada(models.Model):
    producto = models.ForeignKey('Crear_producto', on_delete=models.CASCADE)  # Relación con el producto
    cantidad = models.PositiveIntegerField()  # Cantidad de producto ingresada
    lote = models.CharField(max_length=100, default='')   # Número de lote del producto
    fecha_vencimiento = models.DateField(null=True, blank=True) # Fecha de vencimiento del producto

    def __str__(self):
        return f"{self.producto.nombre_producto} - {self.cantidad} - Lote: {self.lote}"

class CrearProveedor(models.Model):
    id_proveedor = models.CharField(max_length=10, unique=True, editable=False, blank=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    nit = models.CharField(max_length=15, verbose_name="NIT", unique=True)
    direccion = models.TextField(verbose_name="Dirección")
    telefono = models.CharField(max_length=15, verbose_name="Número Telefónico")
    correo_electronico = models.EmailField(verbose_name="Correo Electrónico", unique=True)

    def __str__(self):
        return f"{self.id_proveedor} - {self.nombre}"

    def save(self, *args, **kwargs):
        if not self.id_proveedor:
            self.id_proveedor = f"PROV{''.join(random.choices(string.digits, k=4))}"
            while CrearProveedor.objects.filter(id_proveedor=self.id_proveedor).exists():
                self.id_proveedor = f"PROV{''.join(random.choices(string.digits, k=4))}"
        super(CrearProveedor, self).save(*args, **kwargs)
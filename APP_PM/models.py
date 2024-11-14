
from django.db import models
from django.utils import timezone
import random
import string
class Crear_producto(models.Model):
    LINEA_OPCIONES = [
        ('insecticidas', 'Insecticidas'),
        ('fertilizantes', 'Fertilizantes'),
        ('materia prima', 'Materia Prima'),
        ('insumos', 'Insumos'),
        ('coayudantes', 'Coayudantes'),
        ('gravados', 'Gravados'),
        ('bioinsumos', 'Bioinsumos'),
        ('fungicidas', 'Fungicidas'),
        ('maquila', 'Maquila'),
        ('herbicidas', 'Herbicidas'),
    ]

    GRUPO_OPCIONES = [
        ('Orgánicos', 'Orgánicos'),
        ('Granulados', 'Granulados'),
        ('Líquidos', 'Líquidos'),
        ('Polvo', 'Polvo'),
        ('Materia Prima', 'Materia Prima'),
        ('Insumos', 'Insumos'),
    ]
    UNIDAD_OPCIONES = [
        ('KL', 'Kilo'),
        ('KG', 'Kilogramos'),
        ('Litro', 'Litro'),
        ('GL', 'Galones'),
        ('MIL', 'Milímetros'),
        ('C.C', 'Centímetros Cúbicos'),
    ]

    id_producto = models.CharField(max_length=10, unique=True, editable=False, blank=True)
    nombre_producto = models.CharField(max_length=100)
    linea = models.CharField(max_length=100, choices=LINEA_OPCIONES)  # Valor por defecto
    grupo = models.CharField(max_length=100, choices=GRUPO_OPCIONES)
    unidad = models.CharField(max_length=100, choices=UNIDAD_OPCIONES)
    marca = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_producto

    def save(self, *args, **kwargs):
        if not self.id_producto:
            self.id_producto = ''.join(random.choices(string.digits, k=10))
            while Crear_producto.objects.filter(id_producto=self.id_producto).exists():
                self.id_producto = ''.join(random.choices(string.digits, k=10))
        super(Crear_producto, self).save(*args, **kwargs)

class NotaEntrada(models.Model):
    fecha = models.DateField(default=timezone.now)  # Fecha actual por defecto
    cliente = models.CharField(max_length=100, default='Proecologicos S.A.S')  # Campo de cliente
    producto = models.ForeignKey(Crear_producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.producto.nombre_producto} - {self.cantidad}"

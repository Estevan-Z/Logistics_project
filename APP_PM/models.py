# models.py
from django.db import models
import random
import string

class Crear_producto(models.Model):
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


#NOTA DE ENTRADA
# models.py
from django.db import models

class NotaEntrada(models.Model):
    producto = models.ForeignKey(Crear_producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.producto.nombre_producto} - {self.cantidad}"


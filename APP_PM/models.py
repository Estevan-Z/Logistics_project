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


class Cliente(models.Model):
    TIPOS_IDENTIFICACION = [
        ('NIT', 'Nit'),
        ('CED', 'Cédula de ciudadanía'),
        ('NUI', 'Número único de identificación personal'),
        ('CED_EXT', 'Cédula de extranjero'),
        ('TI', 'Tarjeta de identidad'),
    ]

    TIPO_PERSONA = [
        ('PJ', 'Razón social/persona jurídica'),
        ('PN', 'Persona natural'),
    ]

    SEXO_CHOICES = [
        ('EMP', 'Empresa'),
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    tipo_identificacion = models.CharField(max_length=10, choices=TIPOS_IDENTIFICACION)

    identificacion = models.CharField(max_length=20)
    tipo_persona = models.CharField(max_length=2, choices=TIPO_PERSONA)
    nombre = models.CharField(max_length=100)
    primer_nombre = models.CharField(max_length=50, blank=True, null=True)
    segundo_nombre = models.CharField(max_length=50, blank=True, null=True)
    primer_apellido = models.CharField(max_length=50, blank=True, null=True)
    segundo_apellido = models.CharField(max_length=50, blank=True, null=True)
    razon_social = models.CharField(max_length=100, blank=True, null=True)
    nombre_comercial = models.CharField(max_length=100)
    contacto_responsable = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    pais = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    telefono1 = models.CharField(max_length=15)
    telefono2 = models.CharField(max_length=15, blank=True, null=True)
    sexo = models.CharField(max_length=3, choices=SEXO_CHOICES)
    correo_electronico = models.EmailField()
    declarante_renta = models.BooleanField()
    agente_renta = models.BooleanField()
    autoretenedor = models.BooleanField()
    codigo_postal = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre_comercial or self.nombre
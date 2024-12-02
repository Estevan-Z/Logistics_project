from django import forms
from .models import Crear_producto,NotaEntrada, InsertarProductos,CrearProveedor

#CREAR PRODUCTOS
class CrearProductoForm(forms.ModelForm):
    class Meta:
        model = Crear_producto
        fields = [ 'nombre_producto', 'linea', 'grupo',  'marca']  
        widgets = {
            'linea': forms.Select(attrs={'class': 'form-control'}),  
            'grupo': forms.Select(attrs={'class': 'form-control'}),
            'nombre_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
        }

#INSERTAR PRODUCTOS
class InsertarProductosForm(forms.ModelForm):
    class Meta:
        model = InsertarProductos
        fields = ['archivo']
        widgets = {
            'archivo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


# NOTA ENTRADAS
class NotaEntradaForm(forms.ModelForm):
    producto_nombre = forms.CharField(
        label="Producto",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar producto...'
        })
    )

    cliente = forms.CharField(
        label="Cliente",
        initial="Proecologicos S.A.S",  # Valor predeterminado
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )

    class Meta:
        model = NotaEntrada
        fields = ['producto_nombre', 'lote', 'fecha_vencimiento', 'cantidad', 'cliente']
        widgets = {
            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1
            }),
            'lote': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el lote...'
            }),
            'fecha_vencimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'  # Selector de fecha
            }),
        }

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = CrearProveedor
        fields = ['nombre', 'nit', 'direccion', 'telefono', 'correo_electronico']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del proveedor'}),
            'nit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NIT'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Dirección'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo Electrónico'}),
        }




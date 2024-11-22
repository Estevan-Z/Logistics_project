from django import forms
from .models import Crear_producto,NotaEntrada, InsertarProductos

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
        fields = ['producto_nombre', 'cantidad', 'cliente']
        widgets = {
            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1
            }),
        }



from django import forms
from .models import Crear_producto

# forms.py
from django import forms
from .models import Crear_producto

class CrearProductoForm(forms.ModelForm):
    class Meta:
        model = Crear_producto
        fields = [ 'nombre_producto', 'linea', 'grupo', 'unidad', 'marca']  # Agregamos el campo 'linea'
        widgets = {
            'linea': forms.Select(attrs={'class': 'form-control'}),  # Agregar widget para 'linea'
            'grupo': forms.Select(attrs={'class': 'form-control'}),
            'unidad': forms.Select(attrs={'class': 'form-control'}),
            'nombre_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
        }


# forms.py

from .models import NotaEntrada

# forms.py

from django import forms
from .models import NotaEntrada

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



from django import forms
from .models import Crear_producto

class CrearProductoForm(forms.ModelForm):
    class Meta:
        model = Crear_producto
        fields = ['nombre_producto', 'grupo',  'unidad', 'marca']
        labels = {
        }
        widgets = {
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
    producto_nombre = forms.CharField(label="Producto", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar producto...'}))

    class Meta:
        model = NotaEntrada
        fields = ['producto_nombre', 'cantidad']
        widgets = {
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }


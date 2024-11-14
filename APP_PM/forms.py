from django import forms
from .models import Crear_producto,NotaEntrada

#CREAR PRODUCTOS
class CrearProductoForm(forms.ModelForm):
    class Meta:
        model = Crear_producto
        fields = [ 'nombre_producto', 'linea', 'grupo', 'unidad', 'marca']  
        widgets = {
            'linea': forms.Select(attrs={'class': 'form-control'}),  
            'grupo': forms.Select(attrs={'class': 'form-control'}),
            'unidad': forms.Select(attrs={'class': 'form-control'}),
            'nombre_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
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
        initial="Proecologicos S.A.S", 
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )

    class Meta:
        model = NotaEntrada
        fields = ['cliente', 'producto', 'cantidad', 'fecha']
        widgets = {
            'cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}  # Define tipo "date" para mostrar un selector de fecha
            ),
        }



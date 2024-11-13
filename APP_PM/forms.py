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


from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'identificacion','tipo_identificacion',  'tipo_persona', 'nombre', 
            'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido',
            'razon_social', 'nombre_comercial', 'contacto_responsable', 'direccion',
            'pais', 'ciudad', 'telefono1', 'telefono2', 'sexo', 'correo_electronico',
            'declarante_renta', 'agente_renta', 'autoretenedor', 'codigo_postal'
        ]
        widgets = {
            'tipo_identificacion': forms.Select(choices=Cliente.TIPOS_IDENTIFICACION),
            'tipo_persona': forms.Select(choices=Cliente.TIPO_PERSONA),
            'sexo': forms.Select(choices=Cliente.SEXO_CHOICES),
        }

    def clean(self):
        cleaned_data = super().clean()
        tipo_persona = cleaned_data.get('tipo_persona')
        
        if tipo_persona == 'PN':
            # Persona natural: validar que los nombres y apellidos no están vacíos
            if not cleaned_data.get('primer_nombre') or not cleaned_data.get('primer_apellido'):
                self.add_error('primer_nombre', 'El primer nombre es obligatorio para personas naturales.')
                self.add_error('primer_apellido', 'El primer apellido es obligatorio para personas naturales.')
        elif tipo_persona == 'PJ':
            # Razón social: validar que la razón social no esté vacía
            if not cleaned_data.get('razon_social'):
                self.add_error('razon_social', 'La razón social es obligatoria para personas jurídicas.')
                
        return cleaned_data
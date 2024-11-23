import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CrearProductoForm, InsertarProductosForm
from .models import Crear_producto
from django.contrib import messages

def home(request):
    return render(request, 'Home/home.html')

from django.shortcuts import render, redirect
from .forms import CrearProductoForm

def crear_producto(request):
    if request.method == 'POST':
        form = CrearProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            return redirect('productos_creados', producto_id=producto.id_producto)  # Redirige a la vista con el ID del producto
    else:
        form = CrearProductoForm()

    return render(request, 'Productos/Crear_producto.html', {'form': form})

def productos_creados(request, producto_id):
    producto = get_object_or_404(Crear_producto, id_producto=producto_id)
    return render(request, 'Productos/productos_creados.html', {'producto': producto})

def productos_listado(request):
    query = request.GET.get('q')
    if query:
        productos = Crear_producto.objects.filter(nombre_producto__icontains=query)
    else:
        productos = Crear_producto.objects.all()
    
    return render(request, 'Productos/productos_listado.html', {'productos': productos})

def editar_producto(request, producto_id):
    producto = get_object_or_404(Crear_producto, id_producto=producto_id)
    
    if request.method == 'POST':
        form = CrearProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos_creados', producto_id=producto.id_producto)  
    else:
        form = CrearProductoForm(instance=producto)

    return render(request, 'Productos/Edita_producto.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Crear_producto

def eliminar_producto(request, id_producto):
    producto = get_object_or_404(Crear_producto, id_producto=id_producto)
    producto.delete()
    return redirect('productos_listado')


from django.shortcuts import render, redirect
from .models import NotaEntrada, Crear_producto
from .forms import NotaEntradaForm


def agregar_nota_entrada(request):
    if request.method == 'POST':
        form = NotaEntradaForm(request.POST)
        producto_id = request.POST.get('producto_id')
        
        if form.is_valid() and producto_id:
            nota = form.save(commit=False)
            nota.producto = Crear_producto.objects.get(id=producto_id)
            nota.save()
            return redirect('agregar_nota_entrada')
    else:
        form = NotaEntradaForm()

    notas = NotaEntrada.objects.all()
    return render(request, 'Notas/Nota_Entrada.html', {'form': form, 'notas': notas})

# views.py
from django.http import JsonResponse
from .models import Crear_producto

def buscar_producto(request):
    if 'term' in request.GET:
        qs = Crear_producto.objects.filter(nombre_producto__icontains=request.GET.get('term'))
        productos = list(qs.values('id', 'nombre_producto'))
        return JsonResponse(productos, safe=False)
    return JsonResponse([], safe=False)


def insertar_productos(request):
    if request.method == "POST":
        form = InsertarProductosForm(request.POST, request.FILES)
        if form.is_valid():
            archivo_modelo = form.save()
            file = archivo_modelo.archivo

            try:
                # Leer el archivo Excel
                data = pd.read_excel(file)

                # Validar columnas esperadas
                expected_columns = ['nombre_producto', 'linea', 'grupo', 'marca']
                if not all(col in data.columns for col in expected_columns):
                    messages.error(request, f"El archivo debe contener las columnas: {', '.join(expected_columns)}.")
                    return redirect('insertar_productos')

                # Convertir valores de 'linea' y 'grupo' a formato esperado
                data['linea'] = data['linea'].apply(lambda x: f"{int(x):03}")  # Convertir a '001', '002', etc.
                data['grupo'] = data['grupo'].apply(lambda x: f"{int(x):03}")

                # Validar y crear productos
                for _, row in data.iterrows():
                    if row['linea'] not in dict(Crear_producto.LINEA_OPCIONES):
                        messages.warning(request, f"Valor inválido en columna 'linea': {row['linea']}. Producto omitido.")
                        continue
                    if row['grupo'] not in dict(Crear_producto.GRUPO_OPCIONES):
                        messages.warning(request, f"Valor inválido en columna 'grupo': {row['grupo']}. Producto omitido.")
                        continue

                    # Crear producto
                    Crear_producto.objects.create(
                        nombre_producto=row['nombre_producto'],
                        linea=row['linea'],
                        grupo=row['grupo'],
                        marca=row['marca']
                    )

                archivo_modelo.procesado = True
                archivo_modelo.save()

                messages.success(request, "Los productos fueron insertados exitosamente.")
                return redirect('insertar_productos')

            except Exception as e:
                messages.error(request, f"Error al procesar el archivo: {e}")
                return redirect('insertar_productos')
    else:
        form = InsertarProductosForm()

    return render(request, 'Productos/insertar_productos.html', {'form': form})


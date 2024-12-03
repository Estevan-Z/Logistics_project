import pandas as pd
from xhtml2pdf import pisa
from io import BytesIO
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.contrib import messages
from .forms import CrearProductoForm, InsertarProductosForm, ProveedorForm, NotaEntradaForm
from .models import Crear_producto, NotaEntrada, CrearProveedor

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
    # Recuperar los parámetros de búsqueda y filtro
    query = request.GET.get('q')  # Parámetro de búsqueda
    filtro_marca = request.GET.get('marca')  # Parámetro de filtro por marca

    # Consultar productos
    productos = Crear_producto.objects.all()

    # Aplicar filtros
    if query:
        productos = productos.filter(nombre_producto__icontains=query)  # Búsqueda por nombre
    if filtro_marca:
        productos = productos.filter(marca=filtro_marca)  # Filtro por marca

    # Obtener todas las marcas para los botones dinámicos
    marcas = Crear_producto.objects.values_list('marca', flat=True).distinct()

    # Renderizar la plantilla
    return render(request, 'Productos/productos_listado.html', {
        'productos': productos,
        'marcas': marcas
    })
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

    proveedores = CrearProveedor.objects.all()
    notas = NotaEntrada.objects.all()
    return render(request, 'Notas/Nota_Entrada.html', {'form': form, 'notas': notas, 'proveedores': proveedores})

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
            archivo_modelo = form.save()  # Guarda el archivo
            file = archivo_modelo.archivo

            try:
                # Validar el tipo de archivo
                if not file.name.endswith('.xlsx'):
                    messages.error(request, "El archivo debe ser un archivo de Excel (.xlsx).")
                    return redirect('insertar_productos')

                # Leer el archivo Excel
                data = pd.read_excel(file)

                # Validar columnas esperadas
                expected_columns = ['nombre_producto', 'linea', 'grupo', 'marca']
                if not all(col in data.columns for col in expected_columns):
                    messages.error(request, f"El archivo debe contener las columnas: {', '.join(expected_columns)}.")
                    return redirect('insertar_productos')

                # Diccionarios para convertir nombres a códigos (convertimos claves y valores a minúsculas)
                linea_dict = {k.lower(): v for k, v in dict(Crear_producto.LINEA_OPCIONES).items()}
                grupo_dict = {k.lower(): v for k, v in dict(Crear_producto.GRUPO_OPCIONES).items()}

                # Invertir los diccionarios para buscar por nombre (también insensible a mayúsculas)
                linea_dict_invertido = {v.lower(): k for k, v in linea_dict.items()}
                grupo_dict_invertido = {v.lower(): k for k, v in grupo_dict.items()}

                # Convertir valores de 'linea' y 'grupo'
                for index, row in data.iterrows():
                    # Convertir línea
                    linea_value = str(row['linea']).lower()  # Convertir valor a minúsculas
                    if linea_value in linea_dict:  # Si ya es un código
                        linea_code = linea_value
                    elif linea_value in linea_dict_invertido:  # Si es un nombre
                        linea_code = linea_dict_invertido[linea_value]
                    else:
                        messages.warning(request, f"Valor inválido en columna 'linea' en la fila {index + 2}: {row['linea']}. Producto omitido.")
                        continue

                    # Convertir grupo
                    grupo_value = str(row['grupo']).lower()  # Convertir valor a minúsculas
                    if grupo_value in grupo_dict:  # Si ya es un código
                        grupo_code = grupo_value
                    elif grupo_value in grupo_dict_invertido:  # Si es un nombre
                        grupo_code = grupo_dict_invertido[grupo_value]
                    else:
                        messages.warning(request, f"Valor inválido en columna 'grupo' en la fila {index + 2}: {row['grupo']}. Producto omitido.")
                        continue

                    # Crear producto
                    Crear_producto.objects.create(
                        nombre_producto=row['nombre_producto'],
                        linea=linea_code,
                        grupo=grupo_code,
                        marca=row['marca']
                    )

                # Marcar el archivo como procesado
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


def generar_pdf(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        productos = data.get("productos", [])
        observacion = data.get("observacion", "")
        
        # Preparar los datos para el HTML
        context = {
            "productos": productos,
            "observacion": observacion,
            "fecha": datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
        }

        # Renderizar el template HTML con los datos
        html = render_to_string("Notas/Nota_entrada_pdf.html", context)

        # Crear el PDF a partir del HTML
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = 'inline; filename="NotaEntrada.pdf"'

        pisa_status = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=response, encoding="UTF-8")
        
        # Comprobar si hubo errores al generar el PDF
        if pisa_status.err:
            return HttpResponse("Hubo un error al generar el PDF.", status=500)

        return response
    
def lista_proveedores(request):
    proveedores = CrearProveedor.objects.all()
    return render(request, 'Proveedores/Lista_proveedores.html', {'proveedores': proveedores})

def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')  # Redirige a la lista de proveedores
    else:
        form = ProveedorForm()
    return render(request, 'Proveedores/Crear_proveedor.html', {'form': form})

def buscar_proveedor(request):
    query = request.GET.get('term', '')
    proveedores = CrearProveedor.objects.filter(nombre__icontains=query)
    proveedores_list = [{'label': proveedor.nombre, 'value': proveedor.id_proveedor} for proveedor in proveedores]
    return JsonResponse(proveedores_list, safe=False)


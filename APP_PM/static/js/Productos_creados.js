if (sessionStorage.getItem('productoGuardado') === 'true') {
    // Muestra la alerta con SweetAlert
    Swal.fire({
        position: 'top-end',
        icon: 'success',
        title: '¡Producto guardado correctamente!',
        showConfirmButton: false,
        timer: 1500
    });
    // Borra el indicador de sessionStorage
    sessionStorage.removeItem('productoGuardado');
}


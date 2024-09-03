from django.shortcuts import render

def obtener_nuevo(request):
    return render(request, 'new_app/nuevo.html')

def obtener_listado(request):
    contenido = {
        'lista': [1, 2, 3],
        'otro_valor': 'Tangamandapio'
    }
    return render(request, 'new_app/listado.html', contenido)

def obtener_imagenes(request):
    return render(request, 'new_app/imagenes.html')
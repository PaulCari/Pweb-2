from django.shortcuts import render, get_object_or_404, redirect
from .models import DestinosTuristicos
from .forms import DestinoForm
from django.http import HttpResponse
from reportlab.pdfgen import canvas

# destinos/views.py
def listar_destinos(request):
    destinos = DestinosTuristicos.objects.all()
    print(destinos)  # Debug temporal
    return render(request, 'destinos/listar_destinos.html', {'destinos': destinos})

def añadir_destino(request):
    if request.method == 'POST':
        form = DestinoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_destinos')
    else:
        form = DestinoForm()
    return render(request, 'destinos/añadir_destino.html', {'form': form})


def modificar_destino(request, id):
    destino = get_object_or_404(DestinosTuristicos, id=id)
    if request.method == 'POST':
        form = DestinoForm(request.POST, request.FILES, instance=destino)
        if form.is_valid():
            form.save()
            return redirect('listar_destinos')
    else:
        form = DestinoForm(instance=destino)
    return render(request, 'destinos/modificar_destino.html', {'form': form})


def eliminar_destino(request, id):
    destino = get_object_or_404(DestinosTuristicos, id=id)
    if request.method == 'POST':
        destino.delete()
        return redirect('listar_destinos')
    return render(request, 'destinos/eliminar_destino.html', {'destino': destino})
def generar_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="destinos.pdf"'

    # Crear el objeto PDF
    p = canvas.Canvas(response)

    # Obtener datos de la base de datos o donde estén almacenados
    destinos = DestinosTuristicos.objects.all()

    # Escribir información en el PDF
    y = 800
    for destino in destinos:
        p.drawString(100, y, f"Nombre: {destino.nombre}")
        p.drawString(100, y - 20, f"Descripción: {destino.descripcion}")
        y -= 40

    # Cerrar el objeto PDF
    p.showPage()
    p.save()

    return response

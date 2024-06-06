from django.shortcuts import render, get_object_or_404, redirect
from .models import DestinosTuristicos
from .forms import DestinoForm

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

from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm


def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'core/clientes.html', {'clientes': clientes})


def criar_cliente(request):
    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_clientes')

    return render(request, 'core/cliente-form.html', {'form': form})


def alterar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    form = ClienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('listar_clientes')

    return render(request, 'core/cliente-form.html', {'form': form, 'cliente': cliente})


def excluir_cliente(request, id):
    cliente = Cliente.objects.get(id=id)

    if request.method == 'POST':
        cliente.delete()
        return redirect('listar_clientes')

    return render(request, 'core/cliente-excluir-confirma.html', {'cliente': cliente})
from django.shortcuts import render, redirect
from .forms import TransaksiForm
from .models import Transaksi

def transaksi_list(request):
    transaksi = Transaksi.objects.all()
    return render(request, 'transaksi/transaksi_list.html', {'transaksi': transaksi})

def transaksi_create(request):
    form = TransaksiForm()
    if request.method == 'POST':
        form = TransaksiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaksi_list')
    return render(request, 'transaksi/transaksi_create.html', {'form': form})

def transaksi_update(request, pk):
    transaksi = Transaksi.objects.get(pk=pk)
    form = TransaksiForm(instance=transaksi)
    if request.method == 'POST':
        form = TransaksiForm(request.POST, instance=transaksi)
        if form.is_valid():
            form.save()
            return redirect('transaksi_list')
    return render(request, 'transaksi/transaksi_update.html', {'form': form, 'transaksi': transaksi})

def transaksi_delete(request, pk):
    transaksi = Transaksi.objects.get(pk=pk)
    transaksi.delete()
    return redirect('transaksi_list')

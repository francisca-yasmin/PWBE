from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

def item_read(request): #CRUD -> read
    itens = Item.objects.all()
    return render(request, 'item_read.html', {'itens': itens})

def item_create(request): # CRUD -> create
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_read')
    else:
        form = ItemForm()
    return render(request, 'itens_form.html', {'form': form})

def item_update(request, pk): #CRUD -> U update
    item = get_object_or_404(Item, pk = pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect('item_read')
    else:
        form = ItemForm(instance = item)
    return render(request, 'itens_form.html', {'form': form})

def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_read')
    return render(request, 'confirmar_delete.html', {'item': item})

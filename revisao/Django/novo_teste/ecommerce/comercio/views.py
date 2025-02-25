
from django.shortcuts import render
from .models import Ecommerce

def lista_postagens(request):
 ecommerce = Ecommerce.objects.all().order_by('-produto')
 return render(request, 'comercio/ecommerce.html', {'ecommerce': ecommerce})

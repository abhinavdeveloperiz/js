from django.shortcuts import render
from .models import Products



def home(request):
    products = Products.objects.only('id', 'name', 'image').order_by('-id')
    context = {
        'products': products
    }
    return render(request, 'home.html', context) 


def about(request):
    return render(request, 'about.html')

def products(request):
    products = Products.objects.only('id', 'name', 'image').order_by('-id')
    context = {
        'products': products
    }
    return render(request, 'products.html', context)

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')


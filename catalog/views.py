from django.shortcuts import render
from .models import Product

# Create your views here.
def home_view(request):
    return render(request, 'catalog/home.html')

def contacts_view(request):
    return render(request, 'catalog/contacts.html')

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def product_list(request):

    return render(request, 'catalog/product_list.html', context={})


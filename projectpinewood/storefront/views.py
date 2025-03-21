from django.shortcuts import render
from .models import *

# Create your views here.
def store_landing_view(request):
    return render(request, 'storefront/landing.html')

def product_listing(request):
    products = Product.objects.all()
    return render(request, 'storefront/products.html', {'products': products})
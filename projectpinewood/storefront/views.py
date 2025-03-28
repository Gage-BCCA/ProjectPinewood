from django.shortcuts import render
from .models import *
from .etsy_api import get_etsy_products

# Create your views here.
def store_landing_view(request):
    return render(request, 'storefront/landing.html')


#Could potentially add login requirements here
def product_listing(request):
    products = get_etsy_products()
    if products == True: 
        products = products.get("results", [])
    return render(request, 'storefront/products.html', {"products": products})



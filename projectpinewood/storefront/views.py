from django.shortcuts import render

# Create your views here.
def store_landing_view(request):
    return render(request, 'storefront/landing.html')
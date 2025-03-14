from django.shortcuts import render

# Create your views here.
def homepage_view(request):
    return render(request, "core/index.html")

def about_view(request):
    return render(request, "core/about.html")

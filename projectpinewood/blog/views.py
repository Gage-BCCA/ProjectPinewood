from django.shortcuts import render

# Create your views here.
def blog_landing_view(request):
    return render(request, "blog/example.html")
from django.shortcuts import render

# Create your views here.
def management_landing_view(request):
    return render(request, "management/landing.html")

def management_blog_view(request):
    return render(request, "management/blog/landing.html")

def management_blog_add_post_view(request):
    return render(request, "management/blog/add_post.html")
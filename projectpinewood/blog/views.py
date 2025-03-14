from django.shortcuts import render

# Create your views here.
def blog_landing_view(request):
    return render(request, "blog/landing.html")


def blog_add_post_view(request):
    return render(request, "admin/add_post.html")
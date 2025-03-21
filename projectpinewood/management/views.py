from django.shortcuts import render

# Create your views here.
def management_landing_view(request):
    return render(request, "management/landing.html")

def management_blog_view(request):
    return render(request, "management/blog/landing.html")

def management_blog_add_post_view(request):
    return render(request, "management/blog/add_post.html")

def management_storefront_view(request):
    return render(request, "management/storefront/landing.html")

def management_announcements_view(request):
    return render(request, "management/announcements/landing.html")

def management_newsletter_view(request):
    return render(request, "management/newsletter/landing.html")
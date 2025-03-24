from django.shortcuts import render

# Create your views here.
def management_landing_view(request):
    return render(request, "management/landing.html")

#=================================
# Blog Views
#=================================
def blog_overview(request):
    return render(request, "management/blog/landing.html")

def add_post_view(request):
    return render(request, "management/blog/add_post.html")

def edit_post_view(request):
    return render(request, "management/blog/edit_post.html")

def all_posts_view(request):
    return render(request, "management/blog/all_posts.html")

def delete_post_view(request):
    return render(request, "management/blog/delete_post.html")

#=================================
# Storefront Views
#=================================
def storefront_overview(request):
    return render(request, "management/storefront/landing.html")

def add_featured_product_view(request):
    return render(request, "management/storefront/add_featured_product.html")

def remove_featured_product_view(request):
    return render(request, "management/storefront/remove_featured_product.html")

def all_featured_products_view(request):
    return render(request, "management/storefront/all_featured_products.html")

def edit_featured_product_view(request):
    return render(request, "/management/storefront/edit_featured_product.html")

#=================================
# Announcements Views
#=================================
def announcements_overview(request):
    return render(request, "management/announcements/landing.html")

def all_announcements_view(request):
    return render(request, "management/announcements/all_announcements.html")

def create_announcement_view(request):
    # TODO: Check if an announcement is already present, and display a warning if so
    return render(request, "management/announcements/create_announcement.html")

def remove_current_announcement_view(request):
    return render(request, "management/announcements/remove_current_announcement.html")

def edit_announcement_view(request):
    return render(request, "management/announcements/edit_announcement.html")

#=================================
# Newsletter Views
#=================================
def newsletter_overview(request):
    return render(request, "management/newsletter/landing.html")

def add_email_view(request):
    return render(request, "management/newsletter/add_email.html")

def remove_email_view(request):
    return render(request, "management/newsletter/remove_email.html")

def all_emails_view(request):
    return render(request, "management/newsletter/all_emails.html")

#=================================
# Gallery Views
#=================================
def gallery_overview(request):
    return render(request, "management/gallery/landing.html")

def add_picture_view(request):
    return render(request, "management/gallery/add_picture.html")

def remove_picture_view(request):
    return render(request, "management/gallery/remove_picture.html")

def all_pictures_view(request):
    return render(request, "management/gallery/all_pictures.html")

def edit_picture_view(request):
    return render(request, "management/gallery/edit_picture.html")
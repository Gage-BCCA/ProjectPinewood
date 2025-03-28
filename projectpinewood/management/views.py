from datetime import datetime, timedelta
from operator import truediv

from django.shortcuts import render, redirect
from core.models import Announcement, Subscriber
from blog.models import Post

# Create your views here.
def management_landing_view(request):
    return render(request, "management/landing.html")

#=================================
# Blog Views
#=================================
def blog_overview(request):
    posts = Post.objects.order_by("date_created")[:5]
    context = {
        "posts": posts
    }
    return render(request, "management/blog/landing.html", context=context)

def add_post_view(request):
    return render(request, "management/blog/add_post.html")

def edit_post_view(request):
    return render(request, "management/blog/edit_post.html")

def all_posts_view(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, "management/blog/all_posts.html", context=context)

def delete_post_view(request):
    if request.method == "POST":
        target_id = request.POST.get("id")
        Post.objects.filter(id=id).delete()

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
    context = {}
    active_announcement = Announcement.objects.filter(is_active=True).first()
    context["announcement"] = active_announcement
    return render(request, "management/announcements/landing.html", context=context)

def all_announcements_view(request):
    context = {}
    announcements = Announcement.objects.all()
    context["announcements"] = announcements
    return render(request, "management/announcements/all_announcements.html", context=context)

def create_announcement_view(request):
    if request.method == "POST":
        old_announcements = Announcement.objects.filter(is_active=True)
        for old_announcement in old_announcements:
            old_announcement.is_active = False
            old_announcement.save()

        header = request.POST.get("header")
        subheader = request.POST.get("subheader")
        body = request.POST.get("body")
        expiry = request.POST.get("expiry")
        button_link = request.POST.get("button-link")
        announcement = Announcement (
            header=header,
            subheader=subheader,
            content=body,
            date_expiration = expiry if expiry != "" else None,
            link = button_link,
            is_active = True,
            button_text = "Click now!"
        )
        announcement.save()
        return redirect("management_landing")

    context = {}
    active_announcement = Announcement.objects.filter(is_active=True).first()
    if active_announcement:
        context["announcement_active"] = True
    else:
        context["announcement_active"] = False
    return render(request, "management/announcements/create_announcement.html", context=context)

def remove_current_announcement_view(request):
    if request.method == "POST":
        active_announcement = Announcement.objects.filter(is_active=True).first()
        if active_announcement:
            active_announcement.is_active = False
            active_announcement.save()
        return redirect("management_landing")
    return render(request, "management/announcements/remove_current_announcement.html")

def edit_announcement_view(request):
    context = {}
    active_announcement = Announcement.objects.filter(is_active=True).first()
    if request.method == "POST":
        header = request.POST.get("header")
        subheader = request.POST.get("subheader")
        body = request.POST.get("body")
        expiry = request.POST.get("expiry")
        button_link = request.POST.get("button-link")
        active_announcement.header = header
        active_announcement.subheader = subheader
        active_announcement.content = body
        active_announcement.expiration_date = expiry if expiry != "" else None
        active_announcement.button_link = button_link
        active_announcement.save()
        return redirect("management_landing")

    context["announcement"] = active_announcement
    return render(request, "management/announcements/edit_announcement.html", context=context)

#=================================
# Newsletter Views
#=================================
def newsletter_overview(request):
    context = {}
    subscribers = Subscriber.objects.order_by("date_subscribed")
    recent_subscribers = Subscriber.objects.filter(date_subscribed__gte = datetime.today() - timedelta(days=30))
    context["subscriber_count"] = len(subscribers)
    context["recent_subscriber_count"] = len(recent_subscribers)
    context["subscribers"] = subscribers[:5]
    return render(request, "management/newsletter/landing.html", context=context)

def add_email_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        first_name = request.POST.get("first-name")
        wants_newsletter = request.POST.get("newsletter")
        wants_product_updates = request.POST.get("product-updates")
        new_sub = Subscriber(
            email=email,
            first_name=first_name,
            wants_newsletter=True if wants_newsletter else False,
            wants_product_updates=True if wants_product_updates else False
        )
        new_sub.save()
        return redirect("management_landing")
    return render(request, "management/newsletter/add_email.html")

def remove_email_view(request):
    subscribers = Subscriber.objects.order_by("date_subscribed")
    context = {
        "subscribers": subscribers
    }
    return render(request, "management/newsletter/remove_email.html", context=context)

def all_emails_view(request):
    context = {}
    subscribers = Subscriber.objects.order_by("date_subscribed")
    context["subscribers"] = subscribers
    return render(request, "management/newsletter/all_emails.html", context=context)

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
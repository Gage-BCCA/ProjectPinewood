from django.shortcuts import render
from .models import Announcement
from django.utils import timezone

# Create your views here.
def homepage_view(request):
    context = {}
    announcements = Announcement.objects.filter(date_expiration__gte=timezone.now())
    context["announcements"] = announcements
    return render(request, "core/index.html", context)


def about_view(request):
    return render(request, "core/about.html")


def contact_view(request):
    return render(request, "core/contact.html")

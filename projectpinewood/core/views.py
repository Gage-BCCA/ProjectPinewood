from django.shortcuts import render
from .models import Announcement

# Create your views here.
def homepage_view(request):
    context = {}
    announcements = Announcement.objects.all()
    context["announcements"] = announcements
    return render(request, "core/index.html", context)


def about_view(request):
    return render(request, "core/about.html")


def contact_view(request):
    return render(request, "core/contact.html")

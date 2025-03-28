from django.shortcuts import render, redirect
from .models import Announcement, Subscriber
from .forms import *
from django.utils import timezone

# Create your views here.
def homepage_view(request):
    context = {}
    announcements = Announcement.objects.filter(date_expiration__gte=timezone.now())
    context["announcements"] = announcements
    return render(request, "core/index.html", context)


def about_view(request):
    return render(request, "core/about.html")

def add_subscriber(request):
    context = {}
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            #Can add a redirect here to wherever it wants to go
    else:
        form = SubscriptionForm()
    subscribers = Subscriber.objects.all()
    context = {"form": form, "subscribers": subscribers } #If this needs to be in a template anywhere, I had it for testing


def contact_view(request):
    return render(request, "core/contact.html")

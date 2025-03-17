from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    fields = ["title", "subtitle", "body", "status"]

@admin.register(InterestTag)
class InterestTagsAdmin(admin.ModelAdmin):
    pass

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    fields = ["header", "subheader", "content", "date_expiration", "link"]

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    fields = ['photo', 'date_added', 'is_active']
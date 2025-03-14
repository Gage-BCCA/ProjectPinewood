from django.contrib import admin
from .models import InterestTags, Subscriber

# Register your models here.
@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    fields = ["title", "subtitle", "body", "status"]

@admin.register(InterestTags)
class InterestTagsAdmin(admin.ModelAdmin):
    pass
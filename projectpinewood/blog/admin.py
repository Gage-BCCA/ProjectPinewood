from django.contrib import admin
from .models import Post, PostStatus, Tag

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ["title", "subtitle", "body", "status"]

@admin.register(PostStatus)
class PostStatusAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

from django.db import models
from django.utils.text import slugify


class PostStatus(models.Model):
    status = models.CharField(max_length=255)


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField(default=None, null=True)
    date_last_modified = models.DateTimeField(auto_now=True)
    body = (
        models.TextField()
    )  # TODO: Implement JSON support here instead of regular text
    slug = models.SlugField(unique=True, blank=True)
    featured_image = models.TextField(null=True)  # TODO: Add local image support
    view_count = models.BigIntegerField(default=0)
    status = models.ForeignKey('PostStatus', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

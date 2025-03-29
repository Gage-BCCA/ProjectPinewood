from django.db import models
from django.utils.text import slugify

class Tag(models.Model):
    """Simple tag that helps identify what topics a post covers"""
    tag = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.tag


class PostStatus(models.Model):
    """A status model that's used internally

    Helps determine which posts have been published, or which ones are still
    in progress, soft-deleted, etc.
    """
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.status


# Create your models here.
class Post(models.Model):
    """A model for all blog posts

    Contains several standard fields for the post for display. Also
    contains a few fields for internal use to determine how an article
    is handled.
    """
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField(default=None, null=True)
    date_last_modified = models.DateTimeField(auto_now=True)
    body = (
        models.JSONField()
    )  # TODO: Implement JSON support here instead of regular text
    slug = models.SlugField(unique=True, blank=True)
    featured_image = models.TextField(null=True)  # TODO: Add local image support
    view_count = models.BigIntegerField(default=0)
    status = models.ForeignKey('PostStatus', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')

    def save(self, *args, **kwargs):
        """Overridden save method that slugifies the article's title so it can be used in routing."""
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

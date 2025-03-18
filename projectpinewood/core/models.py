from django.db import models
from django.db.models import ManyToManyField
from django.core.exceptions import ValidationError


# Create your models here.
class InterestTag(models.Model):
    """Tags set during Newsletter sign up.

    Has a many-to-many relationship with the Subscriber model to allow for better insights
    on what content a user wants to see.
    """
    interest_name = models.CharField(max_length=255)

    def __str__(self):
        return self.interest_name


class Subscriber(models.Model):
    """Generic newsletter sign up model

    This models represents a site visitor that has signed up for the newsletter.
    Contains a many-to-many relationship with the InterestTag model, so that
    specific interests can be mapped to specific subscribers.
    """
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    date_subscribed = models.DateTimeField(auto_now_add=True)
    newsletter_delivered = models.IntegerField(default=0)
    interests = ManyToManyField(InterestTag)

    def __str__(self):
        return self.email


class Announcement(models.Model):
    """ Front Page Announcements

    This model represents the announcement that will be displayed on the front
    page. It has an optional expiration date that is checked in the template,
    which will prevent rendering if it has passed. It also has an optional
    link attribute, which will render a button if it is set.
    """
    header = models.CharField(max_length=255, null=False)
    subheader = models.CharField(max_length=255, default=None, null=True, blank=True)
    content = models.TextField(null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_expiration = models.DateTimeField(default=None, null=True, blank=True)
    link = models.URLField(default=None, null=True, blank=True)

    def __str__(self):
        return self.header

max_photo_num = 10 #randomly chosen number
class Gallery(models.Model):
    photo = models.ImageField(upload_to='gallery') #or whatever path you think is best
    date_added = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __self__(self):
        return self.photo
    
    @classmethod
    def get_active_photo_count(cls):
        return cls.objects.filter(is_active=True).count()
    
    def save(self):
        if Gallery.get_active_photo_count() > max_photo_num:
            raise ValidationError

        

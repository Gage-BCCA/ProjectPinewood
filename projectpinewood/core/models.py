from django.db import models
from django.db.models import ManyToManyField


# Create your models here.
class InterestTags(models.Model):
    """
    Tags set during Newsletter sign up.
    Has a many-to-many relationship with the
    Subscriber model to allow for better insights
    on what content a user wants to see.
    """
    interest_name = models.CharField(max_length=255)


class Subscriber(models.Model):
    """
    Generic newsletter sign up model
    """
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    date_subscribed = models.DateTimeField(auto_now_add=True)
    newsletter_delivered = models.IntegerField(default=0)
    interests = ManyToManyField(InterestTags)


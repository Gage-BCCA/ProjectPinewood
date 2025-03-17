from django.db import models

class FeaturedProduct(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    date_added = models.DateTimeField()#auto_now_add=True?
    expiration_date = models.DateTimeField(null=True, blank=True)
    

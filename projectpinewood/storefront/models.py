from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    

class FeaturedProduct(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    date_added = models.DateTimeField()#auto_now_add=True?
    expiration_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.product.title

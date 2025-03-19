from django.db import models

class Product(models.Model):
    listing_id = models.BigIntegerField(unique=True)  
    title = models.CharField(max_length=255)  
    description = models.TextField() 
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    currency_code = models.CharField(max_length=10)
    quantity = models.IntegerField()
    url = models.URLField() 
    image_url = models.URLField(blank=True, null=True)  
    category = models.CharField(max_length=255, blank=True, null=True)
    shop_id = models.BigIntegerField() 
    shop_name = models.CharField(max_length=255)  
    created_at = models.DateTimeField() 
    updated_at = models.DateTimeField(auto_now=True)  
    is_active = models.BooleanField(default=True) 

    def __str__(self):
        return self.title

    

class FeaturedProduct(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    date_added = models.DateTimeField()#auto_now_add=True?
    expiration_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.product.title

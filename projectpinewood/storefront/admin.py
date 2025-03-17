from django.contrib import admin
from .models import *

@admin.register(FeaturedProduct)
class FeaturedProductAdmin(admin.ModelAdmin):
    fields = ('product', 'date_added', 'expiration_date')

    def __str__(self):
        return self.product.title #when product foreign key is created
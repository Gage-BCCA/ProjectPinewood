from django.contrib import admin
from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('id', 'title', 'price', 'date_created')


@admin.register(FeaturedProduct)
class FeaturedProductAdmin(admin.ModelAdmin):
    fields = ('product', 'date_added', 'expiration_date')

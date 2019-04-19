from django.contrib import admin

#models
from .models import *
from django.contrib.auth.models import User 

# Register your models here.
@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display=('pk', 'name', 'number',)
    list_display_links = ('pk',)
    search_fields = ('pk','name', 'number')

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display=('pk', 'product_name', 'price', 'amount', 'status', 'id_provider')
    list_display_links = ('pk', 'product_name')
    search_fields = ('pk','product_name',)

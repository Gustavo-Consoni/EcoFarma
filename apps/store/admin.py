from django.contrib import admin
from apps.store import models


@admin.register(models.Product)
class StoreProductAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'name', 'brand', 'category', 'price', 'total_rating', 'total_reviews', 'stock']
    fields = None


@admin.register(models.ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['name']
    fields = None


@admin.register(models.ProductBrand)
class ProductBrandAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['name']
    fields = None

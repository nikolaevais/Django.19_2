from django.contrib import admin
from catalog.models import Category, Product, Version


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ("id", "name")



@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ("id", "name", "price_per_purchase", "category")
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(Version)
class Version(admin.ModelAdmin):
    list_display = ("id", "product", "version_number", "version_name", "current_version")









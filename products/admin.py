from django.contrib import admin

# Register your models here.
from .models import Category, Product, ProductImage

admin.site.register(Category)

class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product

    inlines = (ProductImageAdmin, )



admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
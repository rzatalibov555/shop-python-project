from django.contrib import admin

# Register your models here.
from .models import Category, Product, ProductImage
from .models import *

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id','name','category','price','discount_persentage','discount_price','created_at')
    list_display_links = ('id','name')
    search_fields = ("name","description")
    # list_editable = ('in_sale',)
    list_filter = ('created_at','category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','created_at')
    list_display_links = ('id','name')
    search_fields = ("name",)


class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    extra = 1



class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product

    inlines = (ProductImageAdmin,)


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product, ProductsAdmin)
admin.site.register(ProductImage,)
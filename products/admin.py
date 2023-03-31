from django.contrib import admin
from django.utils.safestring import mark_safe

import products.models
# Register your models here.
from .models import Category, Product, ProductImage
from .models import *

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id','name','category','price','discount_persentage','discount_price','in_sale','created_at', "first_image")
    list_display_links = ('id','name')
    search_fields = ("name","description")
    # list_editable = ('in_sale',)
    list_filter = ('created_at','category')

    def first_image(self, obj):
        return mark_safe(f"<a target='_blank' href='{obj.productimage_set.first().image.url}'>{obj.productimage_set.first().image.url}</a>") if obj.productimage_set.exists() else None


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','created_at')
    list_display_links = ('id','name')
    search_fields = ("name",)


class ProductImageAdmin(admin.TabularInline): #admin panelde  productun icine salsin deye TabularInline istifade olunur
    model = ProductImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product
    inlines = (ProductImageAdmin,)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductsAdmin)
admin.site.register(ProductImage,)
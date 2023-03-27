from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from django.db.models import F, FloatField
from django.db.models.functions import Coalesce





def index_view(request):

    categories = Category.objects.filter(parent__isnull = True)
    products = Product.objects.annotate(
        discount = Coalesce("discount_price", 0, output_field=FloatField())
    ).annotate(
        total_price = F("price") - F("discount_price")
    ).order_by("-created_at")

    context = {
        "categories": categories,
        "products": products
    }

    return render(request, "products/list.html", context)



def product_detail_view(request, id):

    # product = get_object_or_404(Product, id=id)

    # product = Product.objects.annotate(
    #     discount=Coalesce("discount_price", 0, output_field=FloatField())
    # ).annotate(
    #     total_price=F("price") - F("discount_price")
    # ).order_by("-created_at").get(id=id)

    products = Product.objects.annotate(
        discount=Coalesce("discount_price", 0, output_field=FloatField())
    ).annotate(
        total_price=F("price") - F("discount_price")
    ).order_by("-created_at")

    product = products.get(id=id)

    releated_products = products.filter(category=product.category).exclude(id=product.id)

    context = {
        "product": product,
        "releated_products": releated_products,
        # "releated_products": releated_products[:8], # slice:8 evezi bu formadada yazmaq olar bu terefden
    }
    return render(request, "products/detail.html", context)





# region important

# todo: EDILMELI OLAN TOTDO LIST
# todo: region important ve endregin lazim olar regionlari acib baglamaq ucundur.

# endregion

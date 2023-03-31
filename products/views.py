from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from django.db.models import F, FloatField, Q
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

    return render(request, "products/index.html", context)

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

def product_list_view(request):

    products = Product.objects.annotate(
        discount=Coalesce("discount_price", 0, output_field=FloatField()),
        sorting_price=Coalesce("discount_price", "price", output_field=FloatField())
    ).annotate(
        # total_price=F("price") - F("discount_price")
        total_price=F("price") - F("discount")
    ).order_by("-created_at")

    # print(products.values("price","discount_price","sorting_price"))

    categories = Category.objects.filter(parent__isnull=True)


    category = request.GET.get("category", None)
    # print(f"Category: {category}")
    if category:
        products = products.filter(
            Q(category_id=int(category)) |
            Q(category__parent__id=int(category)) |
            Q(category__parent__parent__id=int(category))
        )

    min_price = request.GET.get("min_price", None)
    max_price = request.GET.get("max_price", None)

    if min_price:
        products = products.filter(sorting_price__gte=min_price)

        # products = products.filter(
        #     Q(discount_price__gte=min_price) |
        #     Q(price__gte=min_price)
        # )

    if max_price:
        products = products.filter(sorting_price__lte=max_price)



    context = {
        "products": products,
        "categories": categories,
    }

    return render(request, "products/list.html", context)



# region important

# todo: EDILMELI OLAN TOTDO LIST
# todo: region important ve endregin lazim olar regionlari acib baglamaq ucundur.

# endregion

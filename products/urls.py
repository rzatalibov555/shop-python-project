from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.index_view, name="index"),
    path("list/", views.product_list_view, name="list"),
    path("detail/<id>/", views.product_detail_view, name="detail"),
]
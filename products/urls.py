from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.index_view, name="index"),
    path("detail/<id>/", views.product_detail_view, name="detail"),
]
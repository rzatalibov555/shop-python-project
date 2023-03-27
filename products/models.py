from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from services.mixins import DateMixin
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from services.uploader import Uploader

User = get_user_model()

class Category(MPTTModel, DateMixin):
    # name = models.CharField(max_length=50, unique=True) # unique=True  - unik olsunlar deye istifade olunur
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name


class Product(DateMixin):

    persentage = (
        (5, '5'),
        (10, '10'),
        (15, '15'),
        (20, '20'),
        (25, '25'),
        (30, '30'),
        (35, '35'),
        (40, '40'),
        (45, '45'),
        (50, '50'),
        (55, '55'),
        (60, '60'),
        (65, '65'),
        (70, '70'),
        (75, '75'),
        (80, '80'),
        (85, '85'),
        (90, '90'),
        (95, '95'),
        (100, '100')
    )


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    description = RichTextField(blank=True, null=True)

    price = models.FloatField()
    in_sale = models.BooleanField(default=False)
    discount_persentage = models.IntegerField(choices=persentage, null=True, blank=True)
    discount_price = models.FloatField(blank=True, null=True)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):  #endirimli qiymeti ozu hesablayir
        if self.in_sale:
            self.discount_price = self.price - (self.price * (self.discount_persentage / 100))
        return super().save(*args, **kwargs)

    # class Meta: # admin terefde products tabledaki cixacaq text
    #     verbose_name = "Mehsul"             # tek halda
    #     verbose_name_plural = "Mehsullar"   # cem halda

# TODO detail icinde price ve persentageleri cixart

class ProductImage(DateMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=Uploader.upload_image_to_product)

    def __str__(self):
        return self.product.name

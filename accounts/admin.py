
from django.contrib import admin
from django.utils.safestring import mark_safe

import products.models
# Register your models here.

from .models import *
# Register your models here.
admin.site.register(MyUser,)
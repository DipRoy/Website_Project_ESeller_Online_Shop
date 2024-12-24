from django.contrib import admin

# Register your models here.
from django.contrib import admin
from order.models import *

# Register your models here.
admin.site.register(Orders)
admin.site.register(OrderItem)

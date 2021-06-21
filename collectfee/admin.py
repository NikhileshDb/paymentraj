from django.contrib import admin, 
from .models import Order
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    date_hierarchy = 'order_date'
    list_display = ('order_product', 'order_amount', 'order_payment_id', 'isPaid', 'order_date')




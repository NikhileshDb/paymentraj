from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_product', 'order_amount', 'order_payment_id', 'isPaid', 'order_date']


@admin.register(ApplicationForm)
class ApplicationFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstName', 'lastName', 'mobile', 'email']


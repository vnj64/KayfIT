from multiprocessing.connection import Client
from django.contrib import admin
from .models import Order_to_Product, Product, Menu, Client, Order

class OrderStateAdmin(admin.ModelAdmin):
    readonly_fields = ('created', )

admin.site.register(Product)
admin.site.register(Menu)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Order_to_Product)
from uuid import uuid4
from django.db import models
from django.utils.translation import gettext_lazy as _

MAX_LENGTH = 255

class Menu(models.Model):
    """Menu model: id, title, restriction_age, products"""

    title = models.CharField(max_length=100, null=True)
    restriction_age = models.DateField(auto_now=False, auto_now_add=False, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "menu"
        verbose_name = _('menu')
        verbose_name_plural = _('menus')

class Product(models.Model):
    """Product model: id, title, description, image, price, url"""

    menu = models.ForeignKey(Menu ,related_name='menu', db_index=True, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='restik/images/')
    price = models.IntegerField(null=True)
    url = models.URLField(blank=True)
    
    def __str__(self):  
        return self.title

    class Meta:
        db_table = "product"
        verbose_name = _('product')
        verbose_name_plural = _('products')

class Client(models.Model):
    """Client model: id, first_name, second_name, address, phone_number"""

    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    address = models.TextField(max_length=250)
    phone_number = models.CharField(max_length=50)
    age = models.DateField(auto_now=False, auto_now_add=False, null=True) 

    def __str__(self):
        return self.first_name + " " + self.second_name

    class Meta:
        db_table = "client"
        verbose_name = _('client')
        verbose_name_plural = _('clients')

class Order(models.Model):
    """Order model: id, product, client, orderstates, important, created"""

    STATES = [
        (1, 'NEW ORDER'),
        (2, 'IN PROCESS'),
        (3, 'READY')
    ]

    product = models.ManyToManyField(Product)
    client = models.ForeignKey(Client, related_name='clients', db_index=True, on_delete=models.CASCADE)
    orderstates = models.PositiveSmallIntegerField(_("orderstates"), choices=STATES, null=True, default=1)
    important = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)    

    def __str__(self):
        return 'Order'   

    class Meta:
        db_table = "order"
        verbose_name = _('order')
        verbose_name_plural = _('orders')

class Order_to_Product(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)


# Нужно добавить REST API ( добавление и удаление заказа, добавление, изменение и удаление продукта) 
# Добавить индексы, работать над страничками
from django.test import TestCase
from .models import Menu, Product, Client, Order

class TestClientModel(TestCase):
    def test_client(self):
        init_kwargs = { 'first_name': 'First name',
                        'second_name': 'Second Name',
                        'address': 'г. Альметьевск, Шашина 29',
                        'phone_number': '89520362525'
                        }
        client = Client.objects.create(**init_kwargs)
        for attr in init_kwargs.keys():
            self.assertEqual(getattr(client, attr), init_kwargs[attr])

class TestMenuModel(TestCase):
    def test_menu(self):
        init_kwargs = { 'title': 'Title',
                        'restriction_age': '2022-04-29'
                        }
        menu = Menu.objects.create(**init_kwargs)
        for attr in init_kwargs.keys():
            self.assertEqual(getattr(menu, attr), init_kwargs[attr])

class TestProductModel(TestCase):
    def test_product(self):
        init_kwargs = { 'title': 'Title',
                        'description': 'Description',
                        'image': 'restik/images/ежик.jpg',
                        'price': 25,
                        'url': 'https://vk.com/feed'
                        }
        product = Product.objects.create(**init_kwargs)
        for attr in init_kwargs.keys():
            self.assertEqual(getattr(product, attr), init_kwargs[attr])
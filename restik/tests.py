from django.test import TestCase

class TestProductModel(TestCase):

    def test_product(self):
        attrs = ['title', 'description', 'image', 'price', 'url']
        values = ['Title', 'Description', 'restik/images/пудж.jpg', 25, '2022-05-16']
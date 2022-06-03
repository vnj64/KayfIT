from django.test import TestCase

# Create your tests here.

from .models import Client

OK=200

class PaymentTestSet(TestCase):

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/payment/')
        self.assertEqual(resp.status_code, OK)

class ProfileTestSet(TestCase):

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/profile/')
        self.assertEqual(resp.status_code, OK)

class SignupTestSet(TestCase):

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/signup/')
        self.assertEqual(resp.status_code, OK)

class LoginTestSet(TestCase):

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/login/')
        self.assertEqual(resp.status_code, OK)

class BasketTestSet(TestCase):

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/basket/')
        self.assertEqual(resp.status_code, OK)

class MainPageTestSet(TestCase):

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, OK)
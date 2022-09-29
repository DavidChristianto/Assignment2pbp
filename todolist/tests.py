from django.test import TestCase, Client
from django.urls import resolve


class ContohAppTest(TestCase):
    def test_html_url_exist(self):
        response = Client().get('/todolist/')
        self.assertEqual(response.status_code,200)

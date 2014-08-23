from django.test import TestCase
from rest_framework.test import APITestCase
from django.core.urlresolvers import reverse
# Create your tests here.
from api.models import Item


class ShareappTests(APITestCase):
    """
    API functions for app login
    """
    fixtures = ['test_data.json']

    def test_anon_logging(self):
        self.assertTrue(Item.objects.count() == 0)

        data = {'message': 'Some message'}
        response = self.client.post(reverse('app_log_message'), data)

        self.assertTrue(response.status_code == 200)
        self.assertTrue(response.content == "1")

        self.assertTrue(Item.objects.count() == 1)
        self.assertTrue(Item.objects.all()[0].message == "Some message")
        self.assertTrue(Item.objects.all()[0].user is None)
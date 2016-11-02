from django.test import TestCase, Client
from rest_framework.test import APIRequestFactory

from views import parse_data


class SimpleTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory(enforce_csrf_checks=True)

    # def test_post(self):
    #     view = parse_data
    #     request = self.factory.post('/predict/')
    #     response = view(request)
    #     response.render()
    #     print("hello: {}".format(response.content))

    def test_post_request_resolves_to_results(self):
        c = Client()
        response = c.post('/predict/',{'payload': 'test string that represents a song'})
        self.assertEqual(response.status_code, 200) 

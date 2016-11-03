from django.test import TestCase, Client

from views import parse_data
import json


class SimpleTest(TestCase):
    def setUp(self):
        self.payload = "want thought was to turn turn  on on "

    # def test_post(self):
    #     view = parse_data
    #     request = self.factory.post('/predict/')
    #     response = view(request)
    #     response.render()
    #     print("hello: {}".format(response.content))

    def test_post_request_resolves_to_results(self):
        c = Client()
        response = c.post('/predict/',self.payload, 'application/json')
        self.assertEqual(response.status_code, 200) 

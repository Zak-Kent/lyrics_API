from django.test import TestCase, Client

from views import parse_data
import json


class SimpleTest(TestCase):
    def setUp(self):
        self.c = Client()

        self.good_payload = "want thought was to turn turn on on"
        self.digit_payload = "6647 3746 888 78 90"
        self.short_payload = "only three words"
        
    def request_helper(self, payload):
        return self.c.post('/predict/',payload, 'application/json')

    def test_post_request_sends_200(self):
        response = self.request_helper(self.good_payload)
        self.assertEqual(response.status_code, 200)

    def test_post_request_returns_object(self):
        response = self.request_helper(self.good_payload)
        output = json.loads(response.content)
        self.assertTrue(type(output) != None)

    def test_good_payload_returns_prediction(self):
        response = self.request_helper(self.good_payload)
        output = json.loads(response.content)
        self.assertEqual(output['year'], 6)

    def test_payload_with_digits_returns_error(self):
        response = self.request_helper(self.digit_payload)
        self.assertEqual(response.status_code, 400)

    def test_short_payload_returns_error(self):
        response = self.request_helper(self.short_payload)
        self.assertEqual(response.status_code, 400)


        

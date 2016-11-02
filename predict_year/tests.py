from django.test import TestCase, Client

from views import parse_data


class SimpleTest(TestCase):
    def setUp(self):
        self.payload = """Don't turn your eyes away And please say that you will stay A while"""

    # def test_post(self):
    #     view = parse_data
    #     request = self.factory.post('/predict/')
    #     response = view(request)
    #     response.render()
    #     print("hello: {}".format(response.content))

    def test_post_request_resolves_to_results(self):
        c = Client()
        response = c.post('/predict/',{'payload': self.payload})
        self.assertEqual(response.status_code, 200) 

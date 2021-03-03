from django.test import TestCase

# Create your tests here.
class TestSchool(TestCase):
    def setUp(self):
        print('setup school')
    def test(self):
        response = self.client.get('/school/api/schools/')
        self.assertEqual(response.status_code, 200, ' fail ')
        print(response.content)

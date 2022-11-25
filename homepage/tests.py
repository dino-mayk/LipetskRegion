from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        with self.subTest('there is a homepage.'):
            response = Client().get('/')
            self.assertEqual(response.status_code, 200)


# python manage.py test homepage

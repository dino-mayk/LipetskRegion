from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        with self.subTest('there is a homepage.'):
            response = Client().get('/')
            self.assertEqual(response.status_code, 200)


class TaskPagesTests(TestCase):
    def test_homepage_show_correct_context(self):
        response = Client().get('/')
        self.assertIn('items', response.context)


# python manage.py test homepage

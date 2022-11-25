from django.shortcuts import reverse
from django.test import TestCase

from feedback.forms import FormFeedback
from feedback.models import Feedback


class FormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = FormFeedback()

    def test_context(self):
        context = {'text': 'тест'}
        form = FormFeedback(data=context)
        self.assertTrue(form.is_valid())

    def test_text_label(self):
        label = FormTests.form.fields['text'].label
        self.assertEquals(label, 'текст')

    def test_text_help_text(self):
        help_text = FormTests.form.fields['text'].help_text
        self.assertEquals(help_text, 'введите ваш текст')

    def test_redirect(self):
        response = self.client.post(
            reverse('feedback:feedback'),
            data={'text': 'тест'}
        )
        self.assertRedirects(response, reverse('feedback:feedback'))


class ModelTests(TestCase):

    def test_new_feedback_object(self):
        feedback_count = Feedback.objects.count()

        self.feedback = Feedback(
            text="тест"
        )
        self.feedback.full_clean()
        self.feedback.save()

        self.assertEqual(Feedback.objects.count(), feedback_count + 1)


# python manage.py test feedback

from django.test import TestCase
from django.core import mail
from django.urls import reverse
import requests


class HomeTests(TestCase):
    # Test home page is accessable
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    # Test is url route in a way to home
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
    # Test template name is correct
    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")


class ThankspageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/thanks/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("thanks"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("thanks"))
        self.assertTemplateUsed(response, "thanks.html")



class SendEmailTestCase(TestCase):
    def test_send_email(self):
        # Prepare test data
        data = {
            'name': 'John Doe',
            'number': '123456789',
            'message': 'Test message',
        }

        # Send a POST request to the view
        response = self.client.post(reverse('send_email'), data)

        # Check the response
        self.assertEqual(response.status_code, 302)  # Expect a redirect

        # Check the email was sent
        self.assertEqual(len(mail.outbox), 1)  # Expect one email to be sent
        email = mail.outbox[0]  # Get the sent email

        # Check the email content
        self.assertEqual(email.subject, "Новый заказ букета!")
        self.assertIn('Новый заказ', email.body)
        self.assertIn('Имя: John Doe', email.body)
        self.assertIn('Номер телефона: 123456789', email.body)
        self.assertIn('Сообщение: Test message', email.body)

        # Check the recipients
        self.assertEqual(email.to, ['lenayar67@gmail.com'])


class TestGallaryExternalLink(TestCase):
    def test_gallary_link(self):
        response = requests.get('https://photos.app.goo.gl/qevqwMiF2Z8zvLHEA')
        self.assertEqual(response.status_code, 200)
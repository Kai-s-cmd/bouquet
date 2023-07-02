from django.test import TestCase
from django.urls import reverse
from .models import Prices


# class HomepageTests(SimpleTestCase):
#     def test_url_exists_at_correct_location(self):
#         response = self.client.get("/")
#         self.assertEqual(response.status_code, 200)

#     def test_url_available_by_name(self):
#         response =self.client.get(reverse('home'))
#         self.assertEqual(response.status_code, 200)

#     def test_template_name_correct(self):
#         response = self.client.get(reverse('home'))
#         self.assertTemplateUsed(response, 'home.html')

#     def test_template_content(self):
#         response = self.client.get(reverse('home'))
#         self.assertContains(response, '<h1>Homepage</h1>')


# class ThankspageTests(SimpleTestCase):
#     def test_url_exists_at_correct_location(self):
#         response = self.client.get("/thanks/")
#         self.assertEqual(response.status_code, 200)

#     def test_url_available_by_name(self):
#         response = self.client.get(reverse("thanks"))
#         self.assertEqual(response.status_code, 200)

#     def test_template_name_correct(self):
#         response = self.client.get(reverse("thanks"))
#         self.assertTemplateUsed(response, "thanks.html")

#     def test_template_content(self):
#         response = self.client.get(reverse("thanks"))
#         self.assertContains(response, "<h1>Спасибо за заказ!</h1>")


class HomeTests(TestCase):
    @classmethod
    # Set up data for order form
    def setUpTestData(cls):
        cls.prices = Prices.objects.create(card_title="This is title!", card_text="This is text!", button_text="This is button!")
    # Test title in form
    def test_model_title(self):
        self.assertEqual(self.prices.card_title, "This is title!")
    # Test text in form
    def test_model_text(self):
        self.assertEqual(self.prices.card_text, "This is text!")
    # Test button in form
    def test_model_button(self):
        self.assertEqual(self.prices.button_text, "This is button!")

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
    # Test order form title
    def test_template_content_of_prices_title(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "This is title!")
    # Test order form text
    def test_template_content_of_prices_text(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "This is text!")
    # Test order form button
    def test_template_content_of_prices_text(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "This is button!")

    

    
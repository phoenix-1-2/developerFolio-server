from django.test import TestCase
from .views import replace, replace_from_template, send_thankyou_mail, send_mail_to_me
from unittest.mock import patch


class ApiTestCase(TestCase):
    def test_replace(self):
        html_content = "<h1>Hello [Name], Nikhil Here !! </h1>"
        search_string = "[Name]"
        replace_string = "Nikhil"
        self.assertEqual(
            replace(html_content, search_string, replace_string),
            "<h1>Hello Nikhil, Nikhil Here !! </h1>",
        )

    def test_replace_from_template(self):
        html_content = "<h1>Hello [Name], Nikhil Here !! </h1>"
        name = "Nikhil"
        self.assertEqual(
            replace_from_template(html_content, name),
            "<h1>Hello Nikhil, Nikhil Here !! </h1>",
        )

    @patch("django.core.mail.EmailMultiAlternatives")
    def test_send_thankyou_mail(self, mock_email):
        user = {
            "name": "Nikhil",
            "email": "",
            "message": "",
        }
        self.assertRaises(Exception, send_thankyou_mail(user))

    @patch("django.core.mail.send_mail")
    def test_send_mail_to_me(self, mock_email):
        user = {
            "name": "Nikhil",
            "email": "",
            "message": "",
        }
        self.assertRaises(Exception, send_mail_to_me(user))

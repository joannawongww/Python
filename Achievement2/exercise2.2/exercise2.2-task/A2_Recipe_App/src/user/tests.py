from django.test import TestCase

# Create your tests here.
# import User model first
from .models import User

# class to write test


class UserModelTest(TestCase):
    # initialize fixed variable
    def setUpTestData():
        # set up non-modified object used by all test
        User.objects.create(username='testuser', password='test123')

    # test if username is initialised
    def test_username_field(self):
        # get user object to test
        user = User.objects.get(id=1)

        # get metadata for 'username' field and query its name
        name_field_label = user._meta.get_field('username').verbose_name

        # compare value to expected result
        self.assertEqual(name_field_label, 'username')

    # test if username field is max 20 char
    def test_username_max_length(self):
        # get user object to test
        user = User.objects.get(id=1)

        # get metadata for 'username' field and query its max length
        max_length = user._meta.get_field('username').max_length

        # compare value to expected result
        self.assertEqual(max_length, 20)

    # test if password field is initialised
    def test_password_field(self):
        # get user object to test
        user = User.objects.get(id=1)

        # get metadata for 'password' field and query its name
        password_field_label = user._meta.get_field('password').verbose_name

        # compare value to expected result
        self.assertEqual(password_field_label, 'password')

    # test if password field is max 20 char
    def test_password_max_length(self):
        # get user object to test
        user = User.objects.get(id=1)

        # get metadata for 'username' field and query its max length
        max_length = user._meta.get_field('password').max_length

        # compare value to expected result
        self.assertEqual(max_length, 20)

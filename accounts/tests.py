from django.test import TestCase, SimpleTestCase
from search.models import CovidUser
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.
class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_signin_page_status_code(self):
        response = self.client.get('/accounts/signin/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response= self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response= self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'accounts/home.html')

class UserTest(TestCase):
    def setUp(self):
        get_user_model().objects.create(username="cotten eye joe", password="password")
        #CovidUser.objects.create(city="copenhagen", country="denmark", user())
    def test_username_content(self):
        user=get_user_model().objects.get(id=1)
        expected_obj_name=f'{user.username}'
        self.assertEqual(expected_obj_name, "cotten eye joe")


class CovidUserTest(TestCase):
    def setUp(self):
        pass
        #get_user_model().objects.create(username="cotten eye joe", password="password")
        #CovidUser.objects.create(city="copenhagen", country="denmark", user())
    def test_username_content(self):
        pass
        # user=get_user_model().objects.get(id=1)
        # expected_obj_name=f'{user.username}'
        # self.assertEqual(expected_obj_name, "cotten eye joe")

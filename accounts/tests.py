from django.test import TestCase, SimpleTestCase
from search.models import CovidUser, City, Country
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.management import call_command
from search.documents import CovidUserDocument
from elasticsearch_dsl import Search
from elasticsearch_dsl import Q

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
        get_user_model().objects.create(username="cotten eye joe", password="password", email="coteye@mail.com")
        #CovidUser.objects.create(city="copenhagen", country="denmark", user())
    def test_username_content(self):
        user=get_user_model().objects.get(email="coteye@mail.com")
        expected_obj_name=f'{user.username}'
        self.assertEqual(expected_obj_name, "cotten eye joe")


class CovidUserTest(TestCase):
    def setUp(self):
        country = Country.objects.create(name="denmark")
        #u1
        city1 =City.objects.create(name="copenhagen", country=country)
        rogan= get_user_model().objects.create(username="joe rogan", password="password")
        CovidUser.objects.create(
            city=city1, 
            country=country, 
            user=rogan,
            has_covid=True
            )

        #u2
        city2 =City.objects.create(name="grevinge", country=country)
        tribbiani= get_user_model().objects.create(username="joey tribbiani", password="password")
        CovidUser.objects.create(
            city=city2, 
            country=country, 
            user=tribbiani,
            has_covid=True
            )
        call_command('search_index', '--rebuild', '-f')

    def test_elasticsearch_singlesearch_homepage(self):
        c = self.client.get(
            "/",data={'countrysearch':"denmark"})
        self.assertEqual(c.context['hits'],2)

    def test_elasticsearch_multisearch_homepage(self):
        c = self.client.get(
            "/",data={'citysearch':"copenhagen", 
            'countrysearch':"denmark"})
        self.assertEqual(c.context['hits'],1)

    def edit_and_search_integration_test(self):
        newuser01=get_user_model().objects.create(username="joe moe", password="password")
        self.client.force_login(user=newuser01)
        c = self.client.post(
            "/accounts/edit/",data={
                'country':"denmark",
                'city':"roskilde",
                "has_covid": True,
                "has_data":False
                })        
        self.assertEqual(c.status_code, 200)
        c = self.client.get(
            "/",data={'countrysearch':"denmark"})
        self.assertEqual(c.context['hits'],3)

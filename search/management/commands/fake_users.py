import random

from dateutil.tz import tz
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.management.base import BaseCommand
from faker import Faker

from search.models import CovidUser, Country, City


# config
User = get_user_model()


class Command(BaseCommand):
    help = 'Create users'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of fake covidusers to be created')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        faker = Faker(['it_IT', 'en_US', 'ja_JP'])

        # create a super user + other simple users
        #User.objects.create_superuser("admin", "admin@admin.com", "admin")
        #[create_profile(faker) for _ in range(4)]

        #users_ids = User.objects.values_list('id', flat=True) 

        for _ in range(count):
            user= create_profile(faker)
            country= create_country(faker)  
            city= create_city(faker, country)
            create_coviduser(faker, user.id, city, country)

        call_command('search_index', '--rebuild', '-f')
        self.stdout.write(self.style.SUCCESS('Successfully ended commands'))

def create_profile(faker, retries=0):
    username = faker.user_name()

    if not User.objects.filter(username=username).exists():
        user = User(username=username, email=faker.email())
        user.set_password(faker.password())
        user.save()
        return user

    elif retries < 3:
        # try again with different random username
        return create_profile(faker, retries + 1)
#
def create_coviduser(faker, users_id, city, country):
    coviduser = CovidUser(
        user_id=users_id,
        city=city,
        country=country,
        created_at=faker.date_time_between(start_date="-10d", end_date="now", tzinfo=tz.gettz('UTC')),
        has_covid=True
    )
    coviduser.save()

def create_city(faker, country):
    city = City(
        name=faker.city(),
        covid_info="",
        country=country
    )
    city.save()
    return city

def create_country(faker):
    country = Country(
        name=faker.country(),
        covid_info="",
    )
    country.save()
    return country

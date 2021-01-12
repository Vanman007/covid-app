from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as logout_django
from django.shortcuts import render, redirect
from .forms import SignUpForm, CovidUserInfoForm
from django.contrib.auth.forms import AuthenticationForm
from search.models import CovidUser, City, Country
from django.contrib.auth import get_user_model
from search.documents import CovidUserDocument
from elasticsearch_dsl import Search
from elasticsearch.exceptions import NotFoundError
from elasticsearch_dsl import Q
from elasticsearch_dsl import A


User=get_user_model()



def home(request):
    city = request.GET.get('citysearch')
    country = request.GET.get('countrysearch')
    if city and country:
        q=(Q("match", city__name=city) & Q("match", city__country__name=country) & Q("match", has_covid=True))
        result = CovidUserDocument.search().query(q)
        context ={
            'country':result.execute().hits[0].city.country.name,
            'city' :result.execute().hits[0].city.name,
            'risk':result.execute().hits[0].city.covid_info,
            'hits': result.count()['value']
            }
    elif country and not city:
        result = CovidUserDocument.search().query("match", city__country__name=country)
        context ={
            'country':result.execute().hits[0].city.country.name,
            'risk':result.execute().hits[0].city.country.covid_info,
            'hits': result.count()['value']
        }
    else:
        context ={}
    return render(request, 'accounts/home.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, "accounts/signin.html",{"form":form})

def logout(request):
    logout_django(request)
    return redirect("home")


def edit(request):
    if request.method == 'POST':
        form = CovidUserInfoForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data.get('city')
            country = form.cleaned_data.get('country')
            has_covid = form.cleaned_data.get('has_covid')
            country, _ = Country.objects.get_or_create(name=country)
            city, _= City.objects.get_or_create(name=city, country=country)
            try:
                obj = CovidUser.objects.get(user__id=request.user.id)
                obj.city=city
                obj.country=country
                obj.has_covid=has_covid
                obj.save()
            except CovidUser.DoesNotExist:
                user = User.objects.get(id=request.user.id)
                obj=CovidUser.objects.create(
                    user=user,
                    city=city, 
                    country=country,
                    has_covid=has_covid
                )
            return render(request,'accounts/edit.html', {"form":form})
    else:
        try:
            obj = CovidUser.objects.get(user__id=request.user.id)    
        except CovidUser.DoesNotExist:
            form = CovidUserInfoForm(initial={'has_data': False})
            return render(request, "accounts/edit.html",{"form":form})
        form = CovidUserInfoForm(
            initial={
                'city':obj.city,
                'country':obj.country,
                'has_covid':obj.has_covid,
                'has_data': True
                }
            )
    return render(request, "accounts/edit.html",{"form":form})
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from search.documents import CovidUserDocument
from elasticsearch_dsl import Search
from elasticsearch.exceptions import NotFoundError
from elasticsearch_dsl import Q
from elasticsearch_dsl import A
import requests


def search(request):
    city = request.GET.get('citysearch')
    country = request.GET.get('countrysearch')
    if city and country:
        print("wrf")
        q=(Q("match", city=city) & Q("match", country=country) & Q("match", has_covid=True))
        result = CovidUserDocument.search().query(q)
        context ={
            'country':result.execute().hits[0].country,
            'city' :result.execute().hits[0].city,
            'risk':result.execute().hits[0].covid_risk,
            'hits': result.count()['value']
            }

    elif country and not city:
        print(country)
        result = CovidUserDocument.search().query("match", country__name=country)
        context ={
            'country':result.execute().hits[0].country,
            'risk':result.execute().hits[0].covid_risk,
            'hits': result.count()['value']
        }
    else:
        context ={}

    return render(request, 'search.html', context)



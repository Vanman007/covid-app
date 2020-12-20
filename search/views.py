from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from search.documents import CovidUserDocument
from elasticsearch_dsl import Search
from elasticsearch.exceptions import NotFoundError

def search(request):
    q = request.GET.get('q')
    
    coviduser = CovidUserDocument.search()
    # for hit in coviduser:
    #     print(hit.country)


    if q:
        result = CovidUserDocument.search().query("match", country=q)
    else:
        result = ""
    #result = PostDocument.search().query("match", contry=q)
    context = {'result':result}

    return render(request, 'search.html', context)

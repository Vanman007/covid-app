from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from search.documents import PostDocument
from elasticsearch_dsl import Search
from elasticsearch.exceptions import NotFoundError

def search(request):
    q = request.GET.get('q')
    #print(q)
    print("been here")
    coviduser = PostDocument.search()
    for hit in coviduser:
        print(hit.country)


    if q:
        result = PostDocument.search().query("match", country=q)
    else:
        result = ""
    #result = PostDocument.search().query("match", contry=q)
    context = {'result':result}

    return render(request, 'search.html', context)

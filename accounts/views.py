from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as logout_django
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from search.documents import CovidUserDocument
from elasticsearch_dsl import Search

def home(request):
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
    return render(request, 'accounts/home.html', {'form': form})

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
    result = CovidUserDocument.search().query("match", userid=request.user.id)
    for i in result:
        print(i.username)    
    context = {}

    return render(request, "accounts/edit.html")
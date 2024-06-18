from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'html/index.html')

def about(request):
    return render(request, 'html/about.html')

def about(request):
    return HttpResponse("Hi, ")

def all_apps(request):
    return render (request, 'all_apps.html')
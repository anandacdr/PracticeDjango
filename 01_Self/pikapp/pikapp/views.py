from django.http import HttpRequest
from django.shortcuts import render

def index(request):
    return render(request, 'html/index.html')


def about(request):
    return render(request, 'html/about.html')
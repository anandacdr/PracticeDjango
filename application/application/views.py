from django.http import HttpResponse

from django.shortcuts import render


def home(request):
    return render(request, 'html/index.html')

def about(request):
    return render(request, 'html/about.html')

from django.shortcuts import render

# Create your views here.
def all_apps(request):
    return render (request, 'apps/all_apps.html')
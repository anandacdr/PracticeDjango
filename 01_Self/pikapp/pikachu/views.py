from django.shortcuts import render

# Create your views here.


def pikachu(request):
    return render(request, 'pikachu/pikachu.html')

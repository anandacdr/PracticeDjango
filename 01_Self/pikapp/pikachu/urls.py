from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pikachu, name="pikachu"),
    path('about/', views.about, name="about"),
]

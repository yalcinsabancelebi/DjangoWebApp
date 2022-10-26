from django.contrib import admin
from django.urls import path
from . import views

app_name="article"

urlpatterns = [
    path('create/',views.index,name="index"),   #sonradan eklenen bu urls.py dosyasında create dizinine istek yapıldığında gitmesi gereken sayfa normal olarak verildi.
]
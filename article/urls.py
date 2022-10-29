from turtle import update
from django.contrib import admin
from django.urls import path
from . import views

app_name="article"

urlpatterns = [
    path('create/',views.index,name="index"),   #sonradan eklenen bu urls.py dosyasında create dizinine istek yapıldığında gitmesi gereken sayfa normal olarak verildi.
    path('dashboard/',views.dashboard,name="dashboard"),
    path('addarticle/',views.addArticle,name="addarticle"),
    path('article/<int:id>',views.detail,name="detail"), #urls de dinamik url yapısı
    path('update/<int:id>',views.update,name="update"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('',views.articles,name="articles"),
]
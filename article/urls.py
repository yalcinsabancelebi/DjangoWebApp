from django.contrib import admin
from django.urls import path
from . import views

app_name="article"

urlpatterns = [
    path('create/',views.index,name="index"),   #sonradan eklenen bu urls.py dosyasında create dizinine istek yapıldığında gitmesi gereken sayfa normal olarak verildi.
    path('dashboard/',views.dashboard,name="dashboard"),
    path('addarticle',views.addArticle,name="addarticle"),
    path('article/<int:id>',views.detail,name="detail") #urls de dinamik url yapısı
]
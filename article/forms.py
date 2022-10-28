from dataclasses import field
from socket import fromshare
from django import forms
from .models import Article #şu anki klasörün altındaki Article yi dahil ettik

class ArticleForm(forms.ModelForm): #django içerinde hazır olarak bulunan model form olarak sayfa içeriğini oluşturuyoruz. kodlar doküman sayfasından alındı
    class Meta:
        model = Article
        fields=['title','content'] #django ya Article içinde tanımlı alanlardan sadece title ve content için textfield oluştumasını istedik
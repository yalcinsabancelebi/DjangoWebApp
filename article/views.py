from ast import keyword
from http.client import NotConnected
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404

import article #httpresponse eklendi
from .forms import ArticleForm
from .models import Article
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def articles(request):
    keyword=request.GET.get("keyword") #requst te GET den gelen get verisindeki "keyword" kısmının verisini aldık
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles":articles})
    articles = Article.objects.all()

    articles=Article.objects.all() #tüm articler alındı
    return render(request,"articles.html",{"articles":articles})


# Create your views here.
def index(request):

    #bu şekilde dict yapısıyla sayfaya veri gönderme yapılıyor
    context={
        "number1":10,
        "number2":[1,2,3,4,5,6,7,8,9,10]
    }

    # return HttpResponse("Anasayfa")
    # veya
    return render(request,"index.html",context) #render ile komple tüm html sayfasını çağırabiliriz (blog klasörü içindeki yolu)
                                                #context yazmak yerine {{"deneme"}} de yazabilirdik
def about(request):
    return render(request,"about.html") #her yeni oluşan html sayfası için bu işlem yapılır

def detail(request,id):
    #article=Article.objects.filter(id = id).first() #request ile gelen articlenin id sini aldık ve first ile ilk sonucu döndürür
    article=get_object_or_404(Article,id=id) #eğer bağlanti hatalı olursa hata sayfası
    return render(request,"detail.html",{"article":article})
    #return HttpResponse("Detail:"+str(id))  #url in düzenlenmesi.her detail çağrıldığında yanıt olarak burdaki kısım dönecek

@login_required(login_url="user:login") #giriş yapmayan kullanıcların ulaşamayacaığı yerleri decorator ile tanımlıyoruz. eğer girmek isterse kullancııyı user ın altındaki login e yönlendiriyoruz
def dashboard(request):
    articles=Article.objects.filter(author=request.user) #sisteme giriş yapmış kişinin makalelerini filtreleyerek articles e atadık
    context={
        "articles":articles
    }
    return render(request,"dashboard.html",context)

@login_required(login_url="user:login") 
def addArticle(request):
    form=ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article=form.save(commit=False) #burda gelen article yi kaydederken author bilgisi vermediğimiz içi hata almamak adına içeriği kaydet ama yollama yaptık
        article.author=request.user #formdan türeyen article ye şuanki oturumdaki user bilgilerini verdik
        article.save()  #kaydettik

        messages.success(request,"Makale Başarıyla Oluşturuldu")
        return redirect("article:dashboard")

    context={
        "form":form
    }
    return render(request,"addarticle.html",context)

@login_required(login_url="user:login") 
def update(request,id):

    article = get_object_or_404(Article,id = id) #Article classındaki mevcut id ile classdaki id si aynı olan articleyi aldık ve atadık
    form = ArticleForm(request.POST or None, request.FILES or None, instance = article) #formun içindeki bilgiler ve dosyalar alındı ve instance ile de yukarıda dolan tüm bilgiler formun içine geldi
    
    if form.is_valid():
        article=form.save(commit=False)
        article.author=request.user
        article.save() 

        messages.success(request,"Makale Başarıyla Güncellendi")
        return redirect("article:dashboard")

    context={
        "form":form
    }
    return render(request,"update.html",context)

@login_required(login_url="user:login") 
def delete(request,id   ):
    article=get_object_or_404(Article,id=id)
    article.delete()

    messages.success(request,"Makale Başarıyla Silindi")
    return redirect("article:dashboard") #article uygulamasından altındaki dashboarda gider

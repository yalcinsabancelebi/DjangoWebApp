from email import message
from importlib.resources import contents
import re
from django.shortcuts import render,redirect #register olduktan sonra anasayfa ya yönlednirmek için dahil edildi
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User #register yapmak için çağırıldı
from django.contrib.auth import login,logout,authenticate #login işlemi için db de kullanıcı var mı yok mu kontrolü için dahil edildi

# Create your views here.
def register(request):

    form=RegisterForm(request.POST or None) #request in GET mi POST mu olduğunu konrol etmeye gerek kalmadan, istek eğer post ise yap yoksa boş döndür anlamında bir ifade yazdık
    if form.is_valid(): #is_valid metotu formsdaki clean metotuna gider ve çalıştrır
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")

        #django shell de olduğu gibi User sinifindan yeni kullanıcı yüretidli ve db ye kaydedlidi
        newUser=User(username =username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser) #django hazır methodu. giriş yapma için
        messages.info(request,"Kayıt İşlemi Başarılı!")
        return redirect("index") #kayıt başarılı olursa views içerindeki "index" adlı sayfaya gidecek
    
    #eğer is_valid() false dönerse boş form sayfası döner
    context={
        "form":form
    }
    return render(request,"register.html",context)





    #yukarıdakilerin aynısı fakat eski yöntem
    """if request.method=="POST": #form isteği post mu
        form=RegisterForm(request.POST) #doğruysa form içeriğinini request ile doldur
        if form.is_valid(): #is_valid metotu formsdaki clean metotuna gider ve çalıştrır
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")

            #django shell de olduğu gibi User sinifindan yeni kullanıcı yüretidli ve db ye kaydedlidi
            newUser=User(username =username)
            newUser.set_password(password)
            newUser.save()
            login(request,newUser) #django hazır methodu. giriş yapma için

            return redirect("index") #kayıt başarılı olursa views içerindeki "index" adlı sayfaya gidecek
        
        context={
            "form":form
        }
        return render(request,"register.html",context)

    else:   #eğer sadece get request gelirse sayfaya boş oluştur
        form = RegisterForm()
        context={
            "form":form
        }
        return render(request,"register.html",context)"""

    """form=RegisterForm()
    context={
        "form":form
    }
    return render(request,"register.html",context)"""

def loginUser(request):
    form=LoginForm(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        #form geçerliyse formdan username ve password bilgisi al
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)
        if user is None:
            messages.info(request,"Kullanıcı Adı veya Şifre Hatalı!")
            return render(request,"login.html",context)

        messages.success(request,"Başarıyla Giriş Yaptınız")
        login(request,user)
        return redirect("index")

    return render(request,"login.html",context)
    #login sayfası oluşturuldu

def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptımız")
    return redirect("index")    #anasayfaya yönderdirme

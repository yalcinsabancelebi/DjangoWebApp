from django.shortcuts import render,HttpResponse #httpresponse eklendi

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
    return HttpResponse("Detail:"+str(id))
"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from article.views import index #article/views de oluşturduğumuz sınıfı burada çağırmak için import ettik
from article import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('detail/<int:id>',views.detail,name="detail"),  #dinamik url tanımlama bu şekilide
    path('articles/',include("article.urls")),  #böyle bir istek olduğunda sonradan oluşturulan farklı bir url dosyasına yönlendirebiliyoruz
    path('user/',include("user.urls")), #yani burda user/login, user/register, user/logout gibi user klasörünün içindeki urls dosyasında bulunan def tetiklenirse çalışcak
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

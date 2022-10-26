from django.contrib import admin
from .models import Article

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display= ["title","author","content","created_date"] #article uygulamasını liste şekilinde istenilen başlıklar halinde listeyebiliyoruz.
    list_display_links=["title","created_date"] #istenilen seçeneğe, link ekler
    search_fields=["title"] #"title" a göre arama çubuğu oluşturur.
    list_filter=["created_date"] #uygulamanın sağ tarafında küçük pencerede "tarihe göre" filtreme yapılabilir

    class Meta:
        model=Article

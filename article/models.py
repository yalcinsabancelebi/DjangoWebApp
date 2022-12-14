from unittest.util import _MAX_LENGTH
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar") #models.CASCADE eğer kullanıcı silinirse ona ait tüm nesneleri de siler. verbose_name görünür ismi değiştirir.
    title=models.CharField(max_length=20,verbose_name="Başlık")
    content=RichTextField()
    created_date=models.DateTimeField(auto_now_add=True,verbose_name="Oluşturma Tarihi")
    article_image=models.FileField(blank=True, null=True, verbose_name="Makaleye resim ekleyin")

    def __str__(self):
        return self.title #article başlığını özel str methoduyla istenilen şekilde gösterme
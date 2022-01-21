from django.db import models
from django.core.files.base import ContentFile
from django.contrib.auth.models import User

# Create your models here.

class post(models.Model):
    post_title = models.CharField(max_length=200, verbose_name='商品名')
    post_image = models.ImageField(upload_to='media/', verbose_name='写真')
    post_price = models.PositiveIntegerField(verbose_name='値段')
    post_address = models.CharField(max_length=200,verbose_name='住所')
    post_date = models.DateTimeField('投稿日時', auto_now_add=True)

    def __str__(self):
        return self.post_title

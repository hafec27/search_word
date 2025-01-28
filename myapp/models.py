from django.db import models
from django.contrib.auth.models import User 

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('miracle', '奇跡'),
        ('amazement', '驚嘆'),
        ('thought', '思索'),
        ('fantasy','幻想'),
        ('strange','奇妙'),
        ('other', 'その他'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    likes = models.PositiveIntegerField(default=0)  # 初期値 0
    created_at = models.DateTimeField(auto_now_add=True)  # 自動生成
    likes = models.IntegerField(default=0)  # いいね数を管理するフィールド

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
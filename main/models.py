from django.contrib.auth.models import User
from django.db import models
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from PIL import Image


class Person(MPTTModel):
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30)
    email = models.EmailField(help_text='Введите правильный адрес эл. почты, пожалуйста.')
    image = models.ImageField(verbose_name='Изоображение')
    birth_date = models.DateField()
    about_us = models.TextField()
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class images(models.Model):
    image = models.ImageField()


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey(
            'self',
            related_name='children',
            on_delete=models.SET_NULL,
            null=True,
            blank=True
        )


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    category = models.ForeignKey(
        Category,
        related_name='post',
        on_delete=models.SET_NULL,
        null=True
    )
    tags = models.ManyToManyField(Tag, related_name='post')
    image = models.ImageField(upload_to='articles/')



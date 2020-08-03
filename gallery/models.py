from django.db import models
from django.forms import TextInput, ImageField


class Image(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название изображения')
    tags = models.CharField(max_length=30, verbose_name='Тэги')
    img = models.ImageField(upload_to='user_image', verbose_name='Загрузите изображение')
    # widgets = dict(title=TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'tttt'
    # }), tags=TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'aaaa'
    # }), img=ImageField())

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Album(models.Model):
    album_title = models.CharField(max_length=20, verbose_name='Название альбома')
    album_image = models.ManyToManyField(Image, verbose_name='Выбор изображения')

    def __str__(self):
        return self.album_title

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
        ordering = ['id']

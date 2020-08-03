from django import forms
from .models import Image, Album


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['title', 'tags', 'img']

    def clean(self):
        cd = self.cleaned_data
        return self.cleaned_data


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        verbose_name = 'Название альбома'
        fields = ['album_title', 'album_image']
        required = False
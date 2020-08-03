from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MyForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Введите Ваше имя')
    last_name = forms.CharField(max_length=30, required=False, help_text='Введите Вашу фамилию')
    email = forms.EmailField(max_length=254, help_text='Введите Вашу электронную почту')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        #labels = {'username': 'Ник', 'first_name': 'Имя',
        #          'last_name': 'Фамилия',  'email': 'Электронная почта',
        #          'password1': 'Пароль', 'password2': 'Подтвердите пароль'}
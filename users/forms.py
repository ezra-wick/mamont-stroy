from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from .models import *
from django.contrib.auth import get_user_model
from django.forms import ModelForm
User = get_user_model()


class ProfileForm(UserCreationForm):
    username=forms.CharField(max_length=191,
                         label='Логин')

    first_name=forms.CharField(max_length=200, 
                               label='Имя', 
                               required=False, 
                               widget=forms.TextInput({ "placeholder": "Иван" }))

    last_name=forms.CharField(max_length=200,
                                label='Фамилия',
                                required=False,
                                widget=forms.TextInput({ "placeholder": "Иванов" }))

    email=forms.EmailField(required=True,
                           max_length=200,
                           label='Email',
                           widget=forms.TextInput({ "placeholder": "ivan@mail.ru" }))

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'email', 'password1', 'password2')



class ProfileFullForm(ModelForm):

    username=forms.CharField(max_length=50,
                             label='Логин')

    first_name=forms.CharField(max_length=200, 
                               label='Имя', 
                               required=False, 
                               widget=forms.TextInput({ "placeholder": "Иван" }))

    last_name=forms.CharField(max_length=200,
                                label='Фамилия',
                                required=False,
                                widget=forms.TextInput({ "placeholder": "Иванов" }))

                                
    address=forms.CharField(max_length=200,
                            label='Адрес',
                            required=False, 
                            widget=forms.Textarea({ "placeholder": "г. Краснознаменск, ул. Победы, дом 6, корп. 5, 1 подъезд, 9 эт., кв.32", 'rows':6,
                                                    'cols':30,
                                                    'style':'resize:none;'}))

    phone=forms.CharField(max_length=200,
                          label='Номер телефона',
                          widget=forms.TextInput({ "placeholder": "+79851234567" }))

    email=forms.EmailField(required=True,
                           max_length=200,
                           label='Email',
                           widget=forms.TextInput({ "placeholder": "ivan@mail.ru" }))
    img=forms.ImageField(required=True,
                           max_length=200,
                           label='Фото',
                           widget=forms.FileInput)                       
    class Meta:
        model = Customer
        fields = ('username', 'first_name','last_name', 'email', 'address', 'phone', 'img')






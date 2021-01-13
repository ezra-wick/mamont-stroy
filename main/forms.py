from django import forms
from django.contrib.auth.forms import User
from django.utils import timezone
from .models import *
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.template.defaultfilters import slugify
User = get_user_model()


class Category_enter(ModelForm):
    categorian=forms.CharField(max_length=200, label='НАЗВАНИЕ',)
    class Meta:
        model = Category
        fields = ('categorian',)
        

class Job_enter(ModelForm):
    
    name = forms.CharField(max_length=200, label='НАЗВАНИЕ', )
    measure = forms.CharField(max_length=200, label='МЕРА ИЗМЕРЕНИЯ',)
    price = forms.DecimalField(label='ЦЕНА',)
    class Meta:
        model = Job
        fields = ('category', 'name', 'measure', 'price',)

class Order_enter(ModelForm):
    name = forms.CharField(max_length=200, label='Имя', widget=forms.TextInput(attrs={'style': 'max-height:30px', 'placeholder':'Ваше имя', 'class': 'jaba jaba-top',}))
    email = forms.EmailField(max_length=200, widget=forms.TextInput(attrs={'style': 'max-height:30px', 'placeholder':'Ваша почта', 'class': 'jaba jaba-top', }))
    phone = forms.DecimalField(max_digits=12, label='Телефон', widget=forms.TextInput(attrs={'style': 'max-height:30px', 'placeholder':'Ваш номер', 'class': 'jaba jaba-top'}))
    text = forms.CharField(label="Сообщение", widget=forms.Textarea(attrs={'style': 'max-height:200px', 'placeholder':'Напишите что мы можем для Вас сделать', 'class': 'jaba jaba-top'}))
    class Meta:
        model = Order
        fields = '__all__'


class Text_editor(ModelForm):
    class Meta:
        model = Post
        fields = { 'text_one', 'text_second', "text_third", "text_four"}
        labels = {
            "text_one": "Первый текст",
            "text_second": "Второй текст",
            "text_third": "Третий текст",
            "text_four": "Четвёртый текст",
        }

        

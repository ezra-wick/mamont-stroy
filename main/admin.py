from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['categorian']


@admin.register(Job)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'measure', 'price',]
    list_filter = ['measure', 'category', 'measure']
    list_editable = ['name', 'measure', 'price']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'text',]
    list_filter = ['name','email', 'phone',]
   
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id',  'text_one', 'text_second', 'text_third', 'text_four']
    list_filter = ['title_name']

@admin.register(Post_Category)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_filter = ['title']
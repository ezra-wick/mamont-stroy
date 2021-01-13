from __future__ import absolute_import, unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from users.decorators import unauthenticated_user, allowed_users, admin_only
from .tasks import order_created, order_created_2

def index(request):
  form = Order_enter()
  orders = Order.objects.all()
  #title = Post_Category.objects.update_or_create(title_name='index')
  title_name = Post_Category.objects.filter(id=1)
  #post = Post.objects.get(id=2)
  post_edit = Text_editor()
  context = {"form": form, 
            'orders':orders, 
            'title_name':title_name,
            #'post':post
}
  if request.method == "POST":
    #post_edit = Text_editor(request.POST)
    form = Order_enter(request.POST)
    #if post_edit.is_valid():
     # post_edit.save()
      #return redirect('/')
    if form.is_valid():
      order = form.save()
      order_created.delay(order.id)
      order_created_2.delay(order.id)
      messages.success(request, f"Отправлено!")
      return redirect('/')
    messages.info(request, "Ошибка в одном из полей. Сообщение не отправлено!")
  return render(request, 'index.html', context)


def about(request):
  title_name = Post_Category.objects.filter(id=3)    
  context = {'title_name':title_name}
  return render (request, 'about.html', context)

def prices(request):
  categories = Category.objects.all()
  products = Job.objects.all()
  context = {'categories':categories, 'products':products}
  return render (request, 'store.html', context)
  
@login_required
@allowed_users(allowed_roles=['managers'])
def prices_enter(request):
  categorians = Category(request)
  products = Job(request)
  form = Category_enter()
  form_2 = Job_enter()
  if request.method == 'POST':
    form = Category_enter(request.POST)
    form_2 = Job_enter(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, f"Категория {categorians.categorian} добавлена!")
 
      return redirect('prices')  
    if form_2.is_valid():
      form_2.save()

      messages.success(request, f"Позиция {products.name} добавлена!")
      return redirect('prices') 


  context = {'categorians':categorians, 'products':products, 'form':form, 'form_2': form_2, 'title':'Добавить категорию и вид работы'}
  return render (request, 'category_job_enter.html', context)


@login_required
@allowed_users(allowed_roles=['managers'])
def category_delete(request, id):
    category_to_delete = Category.objects.get(id=id).delete()
    return redirect("/")

@login_required
@allowed_users(allowed_roles=['managers'])
def category_edit(request, id):
    categorian = get_object_or_404(Category, id=id)
    # добавим в form свойство files
    form = Category_enter(request.POST or None, instance=categorian)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'category_edit.html', {"form": form, "categorian": categorian})


@login_required
@allowed_users(allowed_roles=['managers'])
def product_delete(request, id, name):
    product_to_delete = Job.objects.get(id=id, name=name).delete()
    return redirect("/")

@login_required
@allowed_users(allowed_roles=['managers'])
def product_edit(request, id, name):
    product = get_object_or_404(Job, id=id, name=name)
    form = Job_enter(request.POST or None, instance=product)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'product_edit.html', {"form": form, "product": product})

def uslugi(request):
  title_name = Post_Category.objects.filter(id=2)   
  context = {'title_name':title_name}
  return render (request, 'products.html', context)



@login_required
@allowed_users(allowed_roles=['managers'])
def text_enter(request):
  text = Post(request)
  form_2 = Text_editor()
  if request.method == 'POST':
    form_2 = Text_editor(request.POST)
    if form_2.is_valid():
      form_2.save()
      return redirect('prices') 
  context = {'text':text, 'form_2': form_2,}
  return render (request, 'category_post_enter.html', context)



@login_required
@allowed_users(allowed_roles=['managers'])
def text_one_edit(request, id, title):
    product = get_object_or_404(Post, id=id, title_name=id)
    prod = get_object_or_404(Post, id=id)
    form_2 = Text_editor(request.POST or None, instance=product)
    if request.method == "POST":
        if form_2.is_valid():
            form_2.save()
            return redirect('/')
    return render(request, 'loged_user.html', {"form_2": form_2, "product": product, "prod": prod})


@login_required
@allowed_users(allowed_roles=['managers'])
def text_edit(request, id, title):
    product = get_object_or_404(Post, id=id, title_name=id)
    prod = get_object_or_404(Post, id=id)
    form_2 = Text_editor(request.POST or None, instance=product)
    if request.method == "POST":
        if form_2.is_valid():
            form_2.save()
            return redirect('/')
    return render(request, 'category_post_enter.html', {"form_2": form_2, "product": product, "prod": prod})

def all_text(request):
  form = Order_enter()
  orders = Order.objects.all()
  post = Post.objects.all()
  one_post = Post.objects.filter(id=2)
  context = {
            'post':post,
            'one_post':one_post}

  return render(request, 'list.html', context)
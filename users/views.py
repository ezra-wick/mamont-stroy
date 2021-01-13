from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User, Group
from .decorators import unauthenticated_user, allowed_users, admin_only

@unauthenticated_user
def register (request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            customer=form.save()
            customer.user=request.user
            group = Group.objects.get(name='customers')
            customer.groups.add(group)
            customer.save()
            messages.success(request, f"Создан аккаунт пользователя {request.user.username}")
            return redirect('main:index')    
    context = {'form':form, 'title':'Регистрация нового пользователя'}
    return render(request, 'users/registration.html', context)




@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('index')
		else:
			messages.info(request, 'Логин или пароль неправильные')

	context = {}
	return render(request, 'users/login.html', context)



def logoutPage(request):
	logout(request)
	return redirect('/')

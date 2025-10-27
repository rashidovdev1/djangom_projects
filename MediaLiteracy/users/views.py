from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            messages.error(request, "Parollar mos emas!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Bu foydalanuvchi nomi band!")
            return redirect('register')

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('home')

    return render(request, 'users/register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Login yoki parol xato!")
            return redirect('login')

    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


def profile_view(request):
    return render(request, 'users/profile.html')

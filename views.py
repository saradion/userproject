from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserForm
from .models import User

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'user/templates/user/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username).first()
        if user and user.password == password:
            request.session['user_id'] = user.id
            return redirect('profile')
    return render(request, 'user/templates/user/login.html')

def profile(request):
    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id) if user_id else None
    return render(request, 'user/templates/user/profile.html', {'user': user})

def user_logout(request):
    request.session.flush()
    return redirect('login')
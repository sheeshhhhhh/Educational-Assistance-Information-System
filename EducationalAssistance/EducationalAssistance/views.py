from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# not finish yet
def loginView(request):
    username = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('batch') 
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html', { 'username': username })

# not finish yet
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')
        
        if password != confirm_password:
            messages.error(request, 'Password does not match')
            return render(request, 'register.html', {
                'username': username,
                'email': email
            })

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return render(request, 'register.html', {
                'email': email
            })

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return render(request, 'register.html', {
                'username': username
            })

        user = User.objects.create_user(username, email, password)
        user.save()
        
        return redirect('login')
    
    return render(request, 'register.html')

def logoutView(request):
    logout(request)

    return redirect('login')


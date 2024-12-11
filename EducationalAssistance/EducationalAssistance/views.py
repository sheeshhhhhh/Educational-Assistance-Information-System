from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, AbstractUser

# not finish yet
def loginView(request):
    message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            message = 'Invalid username or password'

    return render(request, 'login.html', {'message': message})

# not finish yet
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect('login')
    return render(request, 'register.html')

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return

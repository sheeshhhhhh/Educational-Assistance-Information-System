from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TeamForm

def homepage(request):
    user = request.user

    return render(request, 'homePage.html', { 'user': user })

def loginView(request):
    if request.user.is_authenticated:
        return redirect('batch') 

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


def register(request):
    if request.user.is_authenticated:
        return redirect('batch') 

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

    return redirect('homepage')

@login_required
def CreateTeam(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.members = request.user
            team.save()

            return redirect('batch')
    else:
        form = TeamForm()

    return render(request, 'team/createTeam.html', { 'form': form })

@login_required
def ConnectTeam(request):
    user = request.user
    if request.method == 'POST':
        newMember = request.POST.get('username')
        
        try:
            newUser = User.objects.get(username=newMember)
            if newUser:
                user.teams.add(newUser)
                return redirect('batch')
        except User.DoesNotExist:
            error = 'User does not Exist'

    return render(request, 'team/connectTeam.html', { 'error': error })
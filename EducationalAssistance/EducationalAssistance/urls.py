"""
URL configuration for EducationalAssistance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('logout/', views.logoutView, name='logout'),
    path('login/', views.loginView, name='login'),
    path('register/', views.register, name='register'),

    path('batch/', include('Batch.urls'), name='batch'),
    path('student/', include('Student.urls'), name='student'),

    path('team/create', views.CreateTeam, name='create_team'),
    path('team/connect', views.ConnectTeam, name='connect_team')
]

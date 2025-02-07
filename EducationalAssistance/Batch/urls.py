from django.urls import path

from . import views

urlpatterns  = [
    path('', views.Batches, name='batch'),
    path('add/', views.AddBatch, name='AddBatch'),
    path('<int:pk>/', views.BatchDetails, name='BatchDetails'),
    path('history/', views.BatchHistory, name='BatchHistory'),
    path('update/<int:pk>/', views.UpdateBatch, name='UpdateBatch'),
    path('cancel/<int:pk>/', views.CancelBatch, name='DeleteBatch'),
]
from django.urls import path

from . import views

urlpatterns  = [
    path('', views.Batches, name='Batches'),
    path('add/', views.AddBatch, name='AddBatch'),
    path('batch/<int:pk>/', views.BatchDetails, name='BatchDetails'),
    path('update/<int:pk>/', views.UpdateBatch, name='UpdateBatch'),
    path('delete/<int:pk>/', views.DeleteBatch, name='DeleteBatch'),
]
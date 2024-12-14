from django.urls import path

from . import views

app_name = 'Batch'
urlpatterns = [
    path('', views.Students, name='Students'),
    path('update/<int:pk>', views.UpdateStudent, name='UpdateStudent'),
    path('delete/<int:pk>', views.DeleteStudent, name='DeleteStudent'),
    path('add/<int:batch_id>', views.AddStudent, name='AddStudent'),
]
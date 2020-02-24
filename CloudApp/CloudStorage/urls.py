from django.urls import path
from . import views # Import the view file. "." means current Directory

urlpatterns = [
    path('', views.home, name = 'App-Home'),
    path('about/', views.about, name = 'App-About'),
    path('upload/', views.upload_file, name = 'File-Upload'),
    path('download/', views.download_file, name = 'File-Download'),
    path('remove/', views.remove_file, name = 'File-Remove')
]

from django.urls import path 
from . import views

app_name = 'notesList'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('notes/', views.NotesView.as_view(), name='notes'),
    path('update', views.UpdateView.as_view(), name='update'),
    path('delete', views.DeleteView.as_view(),name='delete'),
]
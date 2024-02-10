from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import note
from datetime import datetime


class HomeView(TemplateView):
    template_name = 'notesList/home.html'

class NotesView(LoginRequiredMixin, TemplateView):
    login_url = 'members:login'
    template_name = 'notesList/note.html'
    
    def get_context_data(self):
        context = super().get_context_data()
        context["user"] = self.request.user.username
        context["symbol"] = self.request.user.username[:1]
        user = User.objects.get(username=self.request.user.username)
        context["notes"] = note.objects.filter(username=user)
        return context
    
    def post(self, request):
        title = request.POST.get('title')
        notes = request.POST.get('description')
        current_datetime = datetime.now()
        user = User.objects.get(username=request.user.username)
        note.objects.create(username=user, title=title, notes=notes, last_modified = current_datetime)
        return redirect('notesList:notes')
    
class UpdateView(TemplateView):
    template_name = 'notesList/note.html'
    def post(self, request):
        title = request.POST.get('title')
        notes = request.POST.get('description')
        id = request.POST.get('uuid')
        current_datetime = datetime.now()
        note_data = note.objects.all().get(id=id)
        note_data.title = title 
        note_data.notes = notes
        note_data.last_modified = current_datetime
        note_data.save()
        return redirect('notesList:notes')
    
class DeleteView(TemplateView):
    template_name = 'notesList/note.html'
    def post(self, request):
        id = request.POST.get('uuid')
        note_data = note.objects.all().get(id=id)
        note_data.delete()
        return redirect('notesList:notes')
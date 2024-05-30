from django.shortcuts import render, redirect
from . import forms
from .models import Task

# Create your views here.
def add_task(request):
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect ('home')
    else:
        task_form = forms.TaskForm(request.POST)
        
    return render(request, 'add_task.html', {'form': task_form})

def edit_task(request, id):
    task = Task.objects.get(pk=id)
    task_form = forms.TaskForm(instance=task)
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect ('home')
        
    return render(request, 'edit_task.html', {'form': task_form})

def delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('home')
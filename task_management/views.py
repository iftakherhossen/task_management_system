from django.shortcuts import render
from task.models import Task

# Create your views here.
def home(request):
    data = Task.objects.all()
    return render(request, 'home.html', {'data':data})
from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task


def home_page(request):
    if request.method == 'GET':
        tasks = Task.objects.filter(author=request.user)

    return render(request, 'main/HomePage.html', {'tasks': tasks})


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            return redirect('CreateTask')
    else:
        form = TaskForm()

    return render(request, 'main/CreateTask.html', {'form': form})

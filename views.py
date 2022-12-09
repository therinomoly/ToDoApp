from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponseRedirect


# Create your views here.
def todoView(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todoList/index.html', context)


def updateTodo(request, id):
    todos = Todo.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=todos)
    if form.is_valid():
        form.save()
        return redirect('todo')
    return render(request, 'todoList/update.html', {'form': form})


def add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    else:
        form = TaskForm()
    return render(request, 'todoList/add.html', {'form': form})


def delete(request, id):
    todos = Todo.objects.all()
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo')

    return render(request, 'todoList/index.html', {'todos': todos})


def search(request):

    search_term = request.GET.get('search-term') or ''
    todos = Todo.objects.filter(task_name__contains=search_term)

    context = {
        'todos': todos
    }
    return render(request, 'todoList/index.html', context)

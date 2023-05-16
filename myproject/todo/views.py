from django.shortcuts import render, redirect, get_object_or_404
from .forms import TodoForm
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {'todos' : todos})

def add(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm()
    return render(request, 'add.html', {'form': form})

def edit(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'edit.html', {'form': form})

def delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('index')
    return render(request, 'delete_confirm.html', {'todo': todo})

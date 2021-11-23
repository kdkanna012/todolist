from django.shortcuts import render, redirect
from .models import ToDoList

# Create your views here.


def index(request):
    if request.method == 'POST':
        todolist = ToDoList(
            title=request.POST['title']
        )
        todolist.save()
        return redirect('index')

    else:
        todolists = ToDoList.objects.all()
        return render(request, 'index.html', {'todolists': todolists})


def delete_list(request, pk):
    todolist = ToDoList.objects.get(id=pk)
    todolist.delete()
    return redirect('index')

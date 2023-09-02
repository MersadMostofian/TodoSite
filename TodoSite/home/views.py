from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import createTodoForm,updateTodoForm
from .models import Todo
import datetime


def root(request):
    return render(request,'root.htm')
def home(request):
    if request.user.is_authenticated:
        todo = Todo.objects.filter(created_by=request.user).values()
        return render(request, "home2.htm", {"todos": todo})
    else:
        return redirect('user_login')
def detile(request,todo_id):
    todo = Todo.objects.get(id = todo_id)
    return render(request,'detile.htm',{'todo':todo})
def delete(request,todo_id):
    Todo.objects.get(id = todo_id).delete()
    messages.success(request,'Deleted Successfully','success')
    return redirect('homePage')
def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = createTodoForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                Todo.objects.create(title=cd['title'],body=cd['body'],created=str(datetime.datetime.now()),created_by=request.user)
                messages.success(request,'Created Successfully','success')
                return redirect('homePage')
        else:
            form = createTodoForm()
        return render(request,'create.htm',{'form':form})
def update(request,todo_id):
    todo = Todo.objects.get(id = todo_id)
    if request.method == 'POST':
        form = updateTodoForm(request.POST,instance=todo)
        if form.is_valid:
            form.save()
            messages.success(request,'Updated Successfully','success')
            return redirect('detiles',todo_id)
    else:
        form = updateTodoForm(instance=todo)
    return render(request,'update.htm',{'form':form})
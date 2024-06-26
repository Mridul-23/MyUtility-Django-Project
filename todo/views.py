from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from .forms import TODOForm, LoginForm
from .models import TODO
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")

@login_required(login_url='login')
def todo_home(request):
    user = request.user
    form = TODOForm()
    todos = TODO.objects.filter(user=user).order_by('priority')
    return render(request, "todo-home.html", context={"form": form, "todos": todos})

def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", {"form": form})
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("todo:home")
            else:
                error = "Invalid username or password"
        else:
            error = None
        return render(request, "login.html", {"form": form, "error": error})

def signup(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, "signup.html", {"form": form})
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect("login")
        return render(request, "signup.html", {"form": form})

@login_required(login_url='login')
def add_todo(request):
    user = request.user
    form = TODOForm(request.POST)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.user = user
        todo.save()
        return redirect("todo:todo_home")
    else:
        todos = TODO.objects.filter(user=user).order_by('priority')
        return render(request, "todo-home.html", context={"form": form, "todos": todos})

@login_required(login_url='login')
def delete_todo(request, id):
    TODO.objects.get(pk=id).delete()
    return redirect('todo:todo_home')

@login_required(login_url='login')
def change_todo(request, id, status):
    todo = TODO.objects.get(pk=id)
    todo.status = status
    todo.save()
    return redirect('todo:todo_home')

def signout(request):
    auth_logout(request)
    return redirect("login")

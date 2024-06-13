from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django import forms
from app.forms import TODOForm
from app.models import TODO

def home(request):
    form = TODOForm()
    todos = TODO.objects.all()
    return render(request, "home.html",context={'form': form, 'todos': todos})

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, "login.html", {'form': form})
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                error = 'Invalid username or password'
        else:
            error = None
        return render(request, "login.html", {'form': form, 'error': error})


def signup(request):
    if request.method == 'GET':  
        form = UserCreationForm()
        context = {
            "form" : form
        }
        return render(request, "signup.html", context=context)   
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)
        context = {
            "form" : form
        } 
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('login')
        else:
            return render(request, "signup.html", context=context)  
        

def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = TODOForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            print(todo)
            return redirect("home")
        else: 
            return render(request , 'home.html' , context={'form' : form})
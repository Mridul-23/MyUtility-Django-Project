
from django.contrib import admin
from django.urls import path
from app.views import home, login, signup, add_todo, delete_todo, signout


urlpatterns = [
    path("", home, name = 'home'),
    path("home", home),
    path("login", login, name = 'login'),
    path("signup", signup, name = 'signup'),
    path("logout", signout),
    path("add-todo", add_todo),
    path("delete-todo/<int:id>", delete_todo)
]

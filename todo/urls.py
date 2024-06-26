from django.urls import path
from .views import home, todo_home, add_todo, delete_todo, change_todo

app_name = 'todo'

urlpatterns = [
    path("../", home, name='home'),
    path("", todo_home, name='todo_home'),
    path("add-todo/", add_todo, name='add_todo'),
    path("delete-todo/<int:id>/", delete_todo, name='delete_todo'),
    path("change-status/<int:id>/<str:status>/", change_todo, name='change_todo')
]

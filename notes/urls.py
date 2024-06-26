from django.urls import path
from .views import notes, add_note, delete_note

app_name = 'notes' 

urlpatterns = [
    path("", notes, name='notes'),
    path("add-note/", add_note, name='add_note'),
    path("delete-note/<int:id>/", delete_note, name='delete_note'),
]

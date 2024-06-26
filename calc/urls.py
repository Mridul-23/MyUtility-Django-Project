from django.urls import path
from .views import calc

app_name = 'calc'

urlpatterns = [
    path("", calc, name='calc'),
]

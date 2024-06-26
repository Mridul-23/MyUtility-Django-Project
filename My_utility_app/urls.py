from django.contrib import admin
from django.urls import path, include
from todo.views import login, signup, signout, home

urlpatterns = [
    path("", home, name='home'),
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', signout, name='logout'),
    path('todo/', include('todo.urls', namespace='todo')),
    path('notes/', include('notes.urls', namespace='notes')),
    path('calc/', include('calc.urls', namespace='calc')),
    path('weather/', include('weather.urls', namespace='weather')),
]
import requests
from django.shortcuts import render
from .forms import CityForm

def get_weather(request):
    form = CityForm()
    weather_data = None
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            api_key = '9119607966b21e4acf5af337e199b5f9'
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    'city': city,
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon'],
                }
            else:
                weather_data = {'error': 'City not found'}
    
    return render(request, 'weather.html', {'form': form, 'weather_data': weather_data})
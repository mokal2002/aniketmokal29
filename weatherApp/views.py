from django.conf import settings
from django.shortcuts import render, HttpResponse
import requests
from datetime import datetime, timezone, timedelta
import json

# Create your views here.

def weatherApp(request):
    if request.method == "POST":
        city = str(request.POST.get('city'))

        # Enter your "openweathermap.org" API_KEY below
        api_key = settings.API_KEY
        
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        data = requests.get(url).json()
        try:
            if data['cod'] == '404':
                return HttpResponse('{"status": "notfound"}')
            else:
                city_name = data['name']
                country = data.get('sys').get('country', '-')
                ts = data['dt']
                tzone = data['timezone']
                date_time = datetime.fromtimestamp(ts, tz=timezone(timedelta(seconds=tzone))).strftime('%Y-%m-%d')
                temp = int(data['main']['temp'])
                temp_F = format((temp*1.8)+32, '.1f')
                description = data['weather'][0]['description']
                humidity = data['main']['humidity']
                feels_like = int(data['main']['feels_like'])
                wind = format(data['wind']['speed']*3.6, '.1f')
                visibility = format(data['visibility']/1000, '.2f') 

                context = {'status': 'success', 'city': city_name, 'country': country, 'date_time':date_time, 'temp': temp, 'temp_F': temp_F, 'description': description, 'humidity': humidity, 'feels_like': feels_like, 'wind': wind, 'visibility': visibility}
                return HttpResponse(json.dumps(context))
        except:
            return HttpResponse('{"status": "error"}')
            

    return render(request, 'weatherapp/weatherapp.html')

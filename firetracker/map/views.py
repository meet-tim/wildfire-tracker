from django.shortcuts import render
from .models import Fire
import folium
import folium.plugins
import requests

# Create your views here.

def index(request):
    API_KEY = "12333344242"
    
    fires = Fire.objects.all()
    m = folium.Map(location=[24.333,-65.131],tiles="Stamen Terrain",zoom_start=9)
    folium.plugins.Geocoder().add_to(m)

    for fire in fires:
        cd = (fire.lat,fire.lon)
        
        lat = str(fire.lat)
        lon = str(fire.lon)
        BASE_URL = "http://api.openweathermap.org/data/2.5/weather?lat=" + lat+ "&lon=" + lon + "&units=metric&appid={API_KEY}"
        res = requests.get(BASE_URL).json()
        res1 = requests.get("https://api.open-meteo.com/v1/forecast?latitude="+lat+"&longitude="+lon+"&daily=rain_sum&timezone=GMT&past_days=20&forecast_days=1").json()
        print(res1['daily']['rain_sum'][0])

        #calculate days_rain
        count = 0
        days_last_rain = 0
        rain = 0.0
        for i in res1['daily']['rain_sum'][::-1]:         
            if i>0.0:
                days_last_rain+=1
                if count==0:
                    days_last_rain = 0
                rain = i  
                break
            if i == res1['daily']['rain_sum'][0]:
                days_last_rain = 21
            count+=1

        fdi_val = fdi(res['main']['temp'],res['main']['humidity'],res['wind']['speed'],days_last_rain,rain)
        print(fdi_val )
        desc = "<table><t</table>"
        poptext ="<b>Wind speed:</b>" +str(res['wind']['speed']) +"\n" +"<b>wind direction:</b>" + str(res['wind']['deg'])+" deg" + "\n" + "fire danger index:" + str(fdi_val)
        
        folium.Marker(cd,popup=poptext,icon=folium.Icon(color="red", icon="fire")).add_to(m)
        
    
    context = {
        'map':m._repr_html_(),
    }    
    return render(request,'index.html',context)


def fdi(temperature, humidity, wind, days_rain, rain):
    # Calculate factors
    temperature_factor = (temperature - 3) * 6.7
    humidity_factor = (90 - humidity) * 2.6

    if rain <= 0:
        rain = 1
    if days_rain <= 0:
        days_rain = 21
    if wind <= 2:
        wind = 3

    burn_factor = temperature_factor - humidity_factor
    burn_index = (burn_factor / 2 + humidity_factor) / 3.3

    wind_factor = calculate_wind_factor(wind, burn_index)

    if 0 < rain < 2.7:
        if days_rain == 1:
            fdi = wind_factor * 0.7
        elif days_rain == 2:
            fdi = wind_factor * 0.9
        else:
            fdi = wind_factor * 1
    elif 2.7 <= rain < 5.3:
        if days_rain == 1:
            fdi = wind_factor * 0.6
        elif days_rain == 2:
            fdi = wind_factor * 0.8
        elif days_rain == 3:
            fdi = wind_factor * 0.9
        elif days_rain > 3:
            fdi = wind_factor * 1
    elif 5.3 <= rain < 7.7:
        if days_rain == 1:
            fdi = wind_factor * 0.5
        elif days_rain == 2:
            fdi = wind_factor * 0.7
        elif days_rain == 3:
            fdi = wind_factor * 0.9
        elif days_rain == 4:
            fdi = wind_factor * 0.9
        elif days_rain > 4:
            fdi = wind_factor * 1
    elif 7.7 <= rain < 10.3:
        if days_rain == 1:
            fdi = wind_factor * 0.4
        elif days_rain == 2:
            fdi = wind_factor * 0.6
        elif days_rain == 3:
            fdi = wind_factor * 0.8
        elif days_rain == 4:
            fdi = wind_factor * 0.9
        elif days_rain == 5:
            fdi = wind_factor * 0.9
        elif days_rain > 5:
            fdi = wind_factor * 1
    elif 10.3 <= rain < 12.9:
        if days_rain == 1:
            fdi = wind_factor * 0.4
        elif days_rain == 2:
            fdi = wind_factor * 0.6
        elif days_rain == 3:
            fdi = wind_factor * 0.7
        elif days_rain == 4:
            fdi = wind_factor * 0.8
        elif days_rain == 5:
            fdi = wind_factor * 0.9
        elif days_rain == 6:
            fdi = wind_factor * 0.9
        elif days_rain > 6:
            fdi = wind_factor * 1
    elif 12.9 <= rain < 15.4:
        if days_rain == 1:
            fdi = wind_factor * 0.3
        elif days_rain == 2:
            fdi = wind_factor * 0.5
        elif days_rain == 3:
            fdi = wind_factor * 0.7
        elif days_rain == 4:
            fdi = wind_factor * 0.8
        elif days_rain == 5:
            fdi = wind_factor * 0.8
        elif days_rain == 6:
            fdi = wind_factor * 0.9
        elif days_rain > 6:
            fdi = wind_factor * 1
    elif 15.4 <= rain < 20.6:
        if days_rain == 1:
            fdi = wind_factor * 0.2
        elif days_rain == 2:
            fdi = wind_factor * 0.5
        elif days_rain == 3:
            fdi = wind_factor * 0.6
        elif days_rain == 4:
            fdi = wind_factor * 0.7
        elif days_rain == 5:
            fdi = wind_factor * 0.8
        elif days_rain == 6:
            fdi = wind_factor * 0.8
        elif days_rain == 7:
            fdi = wind_factor * 0.9
        elif days_rain == 8:
            fdi = wind_factor * 0.9
        elif days_rain > 8:
            fdi = wind_factor * 1
    elif 20.6 <= rain < 25.6:
        if days_rain == 1:
            fdi = wind_factor * 0.2
        elif days_rain == 2:
            fdi = wind_factor * 0.4
        elif days_rain == 3:
            fdi = wind_factor * 0.5
        elif days_rain == 4:
            fdi = wind_factor * 0.7
        elif days_rain == 5:
            fdi = wind_factor * 0.7
        elif days_rain == 6:
            fdi = wind_factor * 0.8
        elif days_rain == 7:
            fdi = wind_factor * 0.9
        elif days_rain == 8:
            fdi = wind_factor * 0.9
        elif days_rain > 8:
            fdi = wind_factor * 1
    elif 25.6 <= rain < 38.5:
        if days_rain == 1:
            fdi = wind_factor * 0.1
        elif days_rain == 2:
            fdi = wind_factor * 0.3
        elif days_rain == 3:
            fdi = wind_factor * 0.4
        elif days_rain == 4:
            fdi = wind_factor * 0.6
        elif days_rain == 5:
            fdi = wind_factor * 0.6
        elif days_rain == 6:
            fdi = wind_factor * 0.7
        elif days_rain == 7:
            fdi = wind_factor * 0.8
        elif days_rain == 8:
            fdi = wind_factor * 0.8
        elif days_rain == 9:
            fdi = wind_factor * 0.9
        elif days_rain == 10:
            fdi = wind_factor * 0.9
        elif days_rain > 10:
            fdi = wind_factor * 1
    elif 38.5 <= rain < 51.2:
        if days_rain == 1:
            fdi = wind_factor * 0.0
        elif days_rain == 2:
            fdi = wind_factor * 0.2
        elif days_rain == 3:
            fdi = wind_factor * 0.4
        elif days_rain == 4:
            fdi = wind_factor * 0.5
        elif days_rain == 5:
            fdi = wind_factor * 0.5
        elif days_rain == 6:
            fdi = wind_factor * 0.6
        elif days_rain == 7:
            fdi = wind_factor * 0.7
        elif days_rain == 8:
            fdi = wind_factor * 0.7
        elif days_rain == 9:
            fdi = wind_factor * 0.8
        elif days_rain == 10:
            fdi = wind_factor * 0.8
        elif days_rain == 11:
            fdi = wind_factor * 0.9
        elif days_rain == 12:
            fdi = wind_factor * 0.9
        elif days_rain > 12:
            fdi = wind_factor * 1
    elif rain >= 51.2:
        if days_rain == 1:
            fdi = wind_factor * 0.0
        elif days_rain == 2:
            fdi = wind_factor * 0.0
        elif days_rain == 3:
            fdi = wind_factor * 0.1
        elif days_rain == 4:
            fdi = wind_factor * 0.2
        elif days_rain == 5:
            fdi = wind_factor * 0.4
        elif days_rain == 6:
            fdi = wind_factor * 0.5
        elif days_rain == 7:
            fdi = wind_factor * 0.6
        elif days_rain == 8:
            fdi = wind_factor * 0.6
        elif days_rain == 9:
            fdi = wind_factor * 0.6
        elif days_rain == 10:
            fdi = wind_factor * 0.6
        elif days_rain == 11:
            fdi = wind_factor * 0.7
        elif days_rain == 12:
            fdi = wind_factor * 0.7
        elif days_rain == 13:
            fdi = wind_factor * 0.8
        elif days_rain == 14:
            fdi = wind_factor * 0.8
        elif days_rain == 15:
            fdi = wind_factor * 0.8
        elif days_rain == 16:
            fdi = wind_factor * 0.9
        elif days_rain == 17:
            fdi = wind_factor * 0.9
        elif days_rain == 18:
            fdi = wind_factor * 0.9
        elif days_rain == 19:
            fdi = wind_factor * 0.9
        elif days_rain == 20:
            fdi = wind_factor * 0.9
        else:
            fdi = wind_factor * 1

    return round(fdi)


def calculate_wind_factor(wind, burn_index):
    if 0 <= wind < 3:
        return burn_index + 0
    elif 3 <= wind < 9:
        return burn_index + 5
    elif 9 <= wind < 17:
        return burn_index + 10
    elif 17 <= wind < 26:
        return burn_index + 15
    elif 26 <= wind < 33:
        return burn_index + 20
    elif 33 <= wind < 37:
        return burn_index + 25
    elif 37 <= wind < 42:
        return burn_index + 30
    elif 42 <= wind < 46:
        return burn_index + 35
    else:
        return burn_index + 40


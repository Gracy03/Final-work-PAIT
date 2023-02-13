from django.shortcuts import render
import requests
import datetime


# Create your views here.
def index(request):
    if "city" in request.POST:
        city = request.POST['city']
    else:
        city = "Warsaw"
    appid = "92784ff90f2533a54f5f1fe3036f2ad2"
    URL = "https://api.openweathermap.org/data/2.5/weather"
    PARAMS = {"q":city,"appid":appid,"unit":"metric"}
    r = requests.get(url=URL,params = PARAMS)
    res = r.json()
    icon = res['weather'][0]["icon"]
    description = res['weather'][0]["description"]
    temp = res['main']["temp"]
    day = datetime.datetime.today()
    return render(request, "weatherapp/index.html",
                  {'icon': icon,
                   'temp':temp,
                   'description':description,
                   'day':day,
                   'city':city,
                   }
                  )

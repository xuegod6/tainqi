from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import requests

def Index(request):
    return render(request,"index.html")

@csrf_exempt
def Tq(request):
    if request.method == "POST":
        city = request.POST['city']
        url = 'http://api.map.baidu.com/telematics/v3/weather?location={}&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?'.format(
            city)
    else:
        url = 'http://api.map.baidu.com/telematics/v3/weather?location=%E5%8C%97%E4%BA%AC&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?'
    json_data = requests.get(url).json()
    weather = json_data['results'][0]['weather_data']
    today_weather = weather[0]
    t_weather = weather[1]
    tt_weather = weather[2]
    ttt_weather = weather[3]

    city = json_data['results'][0]['currentCity']

    context = {
        'today': today_weather,
        'city': city,
        'list': [t_weather, tt_weather, ttt_weather]
    }
    return JsonResponse({'status':200,'data':context})
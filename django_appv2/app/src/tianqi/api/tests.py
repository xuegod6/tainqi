from django.test import TestCase

# Create your tests here.
import requests

json_data=requests.get("http://api.map.baidu.com/telematics/v3/weather?location={}&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?".format("北京")).json()
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
print(context)
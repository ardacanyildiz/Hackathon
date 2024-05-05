import requests
import geocoder
import pandas as pd
from geopy.geocoders import Nominatim

#defines
df = pd.read_csv('main.csv')
api_key = "1ece4ab017b2b9de11934d4004c72ad7"
playlists = {
    'Thunderstorm' : 'https://fizy.in/pxOcT',
    'Drizzle' : 'https://fizy.in/VZUib',
    'Rain' : 'https://fizy.in/b0Aej',
    'Snow' : 'https://fizy.in/N3mTq',
    'Mist' : 'https://fizy.in/etNSs',
    'Smoke' : 'https://fizy.in/ungXe',
    'Haze': 'https://fizy.in/1rXVf',
    'Dust' : 'https://fizy.in/mTH7Q',
    'Fog' : 'https://fizy.in/LaI4U',
    'Sand' : 'https://fizy.in/rM6BL',
    'Ash' : 'https://fizy.in/mY0GF',
    'Squall' : 'https://fizy.in/8Q2Co', 
    'Tornado' : 'https://fizy.in/W4vai',
    'Clear' : 'https://fizy.in/Y1nWK',
    'Clouds' : 'https://fizy.in/9FEvu'
}
weathers = {
    'Thunderstorm' : 'Fırtına',
    'Drizzle' : 'Çiseleyen Yağmur',
    'Rain' : 'Yağmur',
    'Snow' : 'Karlı',
    'Mist' : 'Buğulu',
    'Smoke' : 'Dumanlı',
    'Haze': 'Puslu',
    'Dust' : 'Tozlu',
    'Fog' : 'Sisli',
    'Sand' : 'Kumlu',
    'Ash' : 'Küllü',
    'Squall' : 'Kasırga', 
    'Tornado' : 'Hortum',
    'Clear' : 'Açık',
    'Clouds' : 'Bulutlu'
}


def loc():
    konum = geocoder.ip('me')
    geoLoc = Nominatim(user_agent="GetLoc")
    latitude = konum.latlng[0]
    longitude = konum.latlng[1]
    locname = geoLoc.reverse(konum.latlng)
    city = locname.address.split(',')[-4]
    loca = {
        'city' : city,
        'lat' : konum.latlng[0],
        'long' : konum.latlng[1]
    }
    return city

def get_weather(api_key, konum):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={konum}&appid={api_key}&units=metric"
    response = requests.get(url)
    veri = response.json()
    if veri["cod"] == 200:
        return veri["weather"][0]['main']
    else:
        print("Bir hata oluştu")
    
city = loc()
weather = get_weather(api_key, city)
print(f"\nŞehir: {city},    Hava Durumu: {weathers[weather]}\n")

if weather in playlists: 
    print(f"İşte senin için mükemmel çalma listesi: {playlists[weather]} \n")
else: 
    print("Bir hata olmuş olmalı, tekrar deneyin")

print("Eğer çalma listesinin içinde ki sarkilari tek olarak dinlemek istersin diye senin için tek tek derledik: \n \n")
asd = df[df['type'] == weather]
for index, row in asd.iterrows():
    print(f"Şarkı adı: {row['name']}" + '    -    ' + f"Şarkıcı adı: {row['artist']}\n")
    
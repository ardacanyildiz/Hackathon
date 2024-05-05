import requests
import geocoder
from datetime import datetime
from geopy.geocoders import Nominatim
import pandas as pd 

df = pd.read_csv('main.csv')

def gunduz():
    print("Zaman: Gündüz\n")
    print("İşte senin için mükemmel çalma listesi: https://fizy.in/gz7Mq") #gündüz
    print("Eğer çalma listesinin içinde ki sarkilari tek olarak dinlemek istersin diye senin için tek tek derledik: \n \n")
    asd = df[df['type'] == 'Day']
    for index, row in asd.iterrows():
        print(f"Şarkı adı: {row['name']}" + '    -    ' + f"Şarkıcı adı: {row['artist']}\n")

def gece():
    print("Zaman: Gece\n")
    print("İşte senin için mükemmel çalma listesi: https://fizy.in/juiht") 
    print("Eğer çalma listesinin içinde ki sarkilari tek olarak dinlemek istersin diye senin için tek tek derledik: \n \n")
    asd = df[df['type'] == 'Night']
    for index, row in asd.iterrows():
        print(f"Şarkı adı: {row['name']}" + '    -    ' + f"Şarkıcı adı: {row['artist']}\n")
        
def get_prayer_times(latitude, longitude):
    today = datetime.today()
    url = f'http://api.aladhan.com/v1/calendar?latitude={latitude}&longitude={longitude}&method=2&month={today.month}&year={today.year}'
    response = requests.get(url)
    data = response.json()
    
    prayer_times = data['data'][0]['timings']
    return prayer_times

def print_prayer_times(prayer_times):
    print("Namaz Vakitleri:")
    for key, value in prayer_times.items():
        print(f"{key.capitalize()}: {value}")

#konum verisini kaydetme
konum = geocoder.ip('me')
geoLoc = Nominatim(user_agent="GetLoc")
latitude = konum.latlng[0]
longitude = konum.latlng[1]


# zamanı kaydetme 
now = datetime.now()
saat = now.hour
dakika = now.minute

#koordinat bilgilerine göre ezan vakitlerini alma
prayer_times = get_prayer_times(latitude, longitude)

# saate çevirme
imsak = prayer_times['Fajr'][:-6].split(':')
for i in range(0, len(imsak)): imsak[i] = int(imsak[i])

aksam = prayer_times['Maghrib'][:-6].split(':')
for i in range(0, len(aksam)): aksam[i] = int(aksam[i])


print(f"Saat: {saat}:{dakika}")

# karşılaştırma
if(saat == imsak[0]) or (saat == aksam[0]):
    if  dakika >= imsak[1] or dakika <= aksam[1]:
        gunduz()
    else:
        gece()
elif(saat > imsak[0]) and (saat < aksam[0]):
    gunduz()
else:
    gece()





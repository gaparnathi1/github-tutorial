import requests
import folium

res = requests.get('https://ipinfo.io/')
data = res.json()
print(data)
IP = data['ip']
loc = data['loc'].split(',')
Region = data['region']
log = float(loc[0])
lat = float(loc[0])
print('IP ADD : ',IP)
print('Log : ', log)
print('Lat : ', lat )
print('Region : ',Region)

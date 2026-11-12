import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=28.6139&longitude=77.209&hourly=temperature_2m&timezone=auto"

response = requests.get(url)

data = response.json()

#print(data["timezone"])
#print (data.keys())
#print (data['hourly'].keys())
print (data['hourly']['time'])
print (data['hourly']['temperature_2m'])
temp = data['hourly']['temperature_2m']
print (temp[0])
time = data['hourly']['time']
print (time[0])

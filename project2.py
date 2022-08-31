# Weather Reports of City using Python
import requests

city = input("Enter your City: ")

print(city)

#Chandigarh

print('Displaying Weather Reports for : ' + city)

url = 'https://wttr.in/{}'.format(city)

res = requests.get(url)

print(res.text)
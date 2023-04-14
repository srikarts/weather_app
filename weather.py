import requests

API_KEY = 'de3f08653494e0df37226ebe0beb3bd1'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def weather():
	city = input("Enter your city name: ")
#lat = 13.2025
#lon = 78.7376
	request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
	response = requests.get(request_url)

	if response.status_code == 200:
		data = response.json()
		print(data)
		print(' ')
		co_ord = data['coord']['lat']
		coordi = data['coord']['lon']
		print(city.upper(),co_ord,coordi)
		weather = data["weather"][0]["description"]
		print(weather)
		temperature = round(data["main"]['temp'] - 273.15,2)
		print(temperature,'°C')

	else:
		print("An error occured.")

weather()






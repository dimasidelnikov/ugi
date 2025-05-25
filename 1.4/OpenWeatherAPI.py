import requests

API_KEY = "9f1270e5b861427e470a17a8ddcaaaa5"
CITY = "Kyiv"
url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(f"Температура у {CITY}: {data['main']['temp']}°C")
else:
    print("Помилка отримання даних")
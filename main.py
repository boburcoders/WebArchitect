import requests
city = input("Enter City: ")
url = f"https://webarchitect.onrender.com/weather/{city}/"
response = requests.get(url)
print(response.text)
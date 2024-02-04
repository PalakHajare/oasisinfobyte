# Importing the 'requests' module to make HTTP requests
import requests

print("\n----------------WEATHER APP----------------\n")

# Setting up constants for the OpenWeatherMap API
Base_URL = "https://api.openweathermap.org/data/2.5/weather?"
Api_KEY = "3388164df1639df43faa856864458835"

# Taking user input for the city name
City = input("Enter the name of location  ")

# Function to convert temperature from Kelvin to Celsius
def converting_to_celcius(kelvin):
    celcius = kelvin - 273
    return celcius

# Constructing the URL for the API request
url = Base_URL + "appid=" + Api_KEY + "&q=" + City

# Making the API request and parsing the JSON response
response = requests.get(url).json()

# Extracting relevant weather information from the response
temp_kelvin = response["main"]["temp"]
temp_celcius = converting_to_celcius(temp_kelvin)
humidity = response["main"]["humidity"]
pressure = response["main"]["pressure"]
feels_like = response["main"]["feels_like"]
feels_like_celcius = converting_to_celcius(feels_like)
max_temp = response["main"]["temp_max"]
min_temp = response["main"]["temp_min"]
max_temp_celcius = converting_to_celcius(max_temp)
min_temp_celcius = converting_to_celcius(min_temp)

# Displaying the weather information for the entered city
print(f"Data for {City} is \n")
print(f"TEMPERATURE is: {temp_celcius} Celcius  ")
print(f"MAX TEMP was: {max_temp_celcius} Celcius ")
print(f"MIN TEMP was: {min_temp_celcius} Celcius ")
print(f"FEELS LIKE: {feels_like_celcius} ")
print(f"PRESSURE: {pressure} mbar ")
print(f"HUMIDITY: {humidity}% ")

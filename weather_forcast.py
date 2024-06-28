import requests
import tkinter as tk
from tkinter import messagebox

# Function to fetch and display weather data
def get_weather():
    target_city = city_entry.get()

    if not target_city:
        messagebox.showerror("Error", "Please enter a city name.")
        return

    api_key = "93d4639be3d12e9f15bf21883d8c3b90"

    geocoding_url = f"http://api.openweathermap.org/geo/1.0/direct?q={target_city}&limit=1&appid={api_key}"
    geocoding_response = requests.get(geocoding_url)
    geocoding_data = geocoding_response.json()

    if geocoding_response.status_code == 200 and geocoding_data:
        lat = geocoding_data[0]['lat']
        lon = geocoding_data[0]['lon']

        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_key}"
        weather_response = requests.get(weather_url)

        if weather_response.status_code == 200:
            weather_data = weather_response.json()
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            pressure = weather_data['main']['pressure']
            precipitation = weather_data.get('rain', {}).get('1h', 0)  

            # Update the labels with fetched data
            temp_label.config(text=f"Temperature: {temperature}°C")
            humidity_label.config(text=f"Humidity: {humidity}%")
            wind_speed_label.config(text=f"Wind Speed: {wind_speed} m/s")
            pressure_label.config(text=f"Pressure: {pressure} hPa")
            precipitation_label.config(text=f"Precipitation: {precipitation} mm")
        else:
            messagebox.showerror("Error", f"Error getting the weather data: {weather_response.status_code}")
    else:
        messagebox.showerror("Error", f"Error getting the geocoding data: {geocoding_response.status_code}")

# Tkinter UI setup
window = tk.Tk()
window.title("Weather Forecast")
window.minsize(width=800, height=600)

city_label = tk.Label(window, text="Enter City Name:")
city_label.pack()

city_entry = tk.Entry(window)
city_entry.pack()

search_btn = tk.Button(window, text="Search", command=get_weather)
search_btn.pack()

temp_label = tk.Label(window, text="Temperature:")
temp_label.pack()

humidity_label = tk.Label(window, text="Humidity:")
humidity_label.pack()

wind_speed_label = tk.Label(window, text="Wind Speed:")
wind_speed_label.pack()

pressure_label = tk.Label(window, text="Pressure:")
pressure_label.pack()

precipitation_label = tk.Label(window, text="Precipitation:")
precipitation_label.pack()

window.mainloop()

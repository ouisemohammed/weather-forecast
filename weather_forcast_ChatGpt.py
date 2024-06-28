import tkinter as tk
from tkinter import messagebox
import requests

WEATHER_API_KEY = '93d4639be3d12e9f15bf21883d8c3b90'

def fetch_weather(location):
    location = location.strip().capitalize()
    api_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={WEATHER_API_KEY}&units=metric'
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        messagebox.showerror("Error", f"Cannot find weather data for {location}. Error code: {response.status_code}")

def update_weather_display():
    location = location_entry.get()
    if not location:
        messagebox.showerror("Error", "Please enter a location.")
        return
    weather_data = fetch_weather(location)
    if weather_data:
        try:
            temperature_label.config(text=f"Temperature: {weather_data['main']['temp']} °C")
            humidity_label.config(text=f"Humidity: {weather_data['main']['humidity']} %")
            wind_label.config(text=f"Wind Speed: {weather_data['wind']['speed']} km/h")
            precipitation = weather_data.get('rain', {}).get('1h', 0)
            precipitation_label.config(text=f"Precipitation: {precipitation} %")
            pressure_label.config(text=f"Pressure: {weather_data['main']['pressure']} hPa")
        except KeyError as e:
            messagebox.showerror("Error", f"Error parsing weather data: Missing key {e}")

def on_enter_key(event):
    update_weather_display()

# Initialize the main window
app = tk.Tk()
app.title("Weather Forecast")
app.geometry("600x400")

# Create and place the widgets
location_label = tk.Label(app, text="Location:", font=('Arial', 14))
location_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

location_entry = tk.Entry(app, font=('Arial', 14), width=20)
location_entry.grid(row=0, column=1, padx=10, pady=10)
location_entry.bind("<Return>", on_enter_key)

search_button = tk.Button(app, text="Search", font=('Arial', 12), command=update_weather_display)
search_button.grid(row=0, column=2, padx=10, pady=10)

temperature_label = tk.Label(app, text="Temperature: N/A", font=('Arial', 14))
temperature_label.grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky='w')

humidity_label = tk.Label(app, text="Humidity: N/A", font=('Arial', 14))
humidity_label.grid(row=2, column=0, columnspan=3, padx=10, pady=5, sticky='w')

wind_label = tk.Label(app, text="Wind Speed: N/A", font=('Arial', 14))
wind_label.grid(row=3, column=0, columnspan=3, padx=10, pady=5, sticky='w')

pressure_label = tk.Label(app, text="Pressure: N/A", font=('Arial', 14))
pressure_label.grid(row=4, column=0, columnspan=3, padx=10, pady=5, sticky='w')

precipitation_label = tk.Label(app, text="Precipitation: N/A", font=('Arial', 14))
precipitation_label.grid(row=5, column=0, columnspan=3, padx=10, pady=5, sticky='w')

# Run the application
app.mainloop()

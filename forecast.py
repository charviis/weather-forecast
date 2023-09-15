import tkinter as tk
import requests

def get_weather():
    city = city_entry.get()
    api_key = "02f58d74d2014ec45cd93186064f9142"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"  # Change units as needed

    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        weather_desc = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        result_label.config(text=f"Weather in {city}:\n{weather_desc}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s")
    else:
        result_label.config(text="City not found or an error occurred.")

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create and configure widgets
city_label = tk.Label(root, text="Enter City:")
city_entry = tk.Entry(root)
search_button = tk.Button(root, text="Search", command=get_weather)
result_label = tk.Label(root, text="", wraplength=300)

# Place widgets in the window
city_label.pack()
city_entry.pack()
search_button.pack()
result_label.pack()

# Start the GUI main loop
root.mainloop()

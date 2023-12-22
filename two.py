import numpy as np

def calculate_weather(wind, pressure, humidity):
    # We use x and y for representing time and temperature
    x = np.linspace(-10, 10, 100)
    y = wind * x**2 + pressure * x + humidity  # Quadratic equation written in terms of weather report
    return x, y

wind = 9
pressure = 7
humidity = 2

x_values, y_values = calculate_weather(wind, pressure, humidity)

print("Generated Weather Data for a Single Set of Inputs:")
for i in range(len(x_values)):
    print(f"x={x_values[i]}, y={y_values[i]}")

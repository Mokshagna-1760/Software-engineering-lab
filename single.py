import numpy as np
import pandas as pd

def calculate_weather(wind, pressure, humidity):
    x = np.linspace(-10, 10, 100)
    y = wind * x**2 + pressure * x + humidity
    return x, y

data = pd.read_csv('three.csv')

for index, row in data.iterrows():
    wind = row['a']
    pressure = row['b']
    humidity = row['c']
    
    x_values, y_values = calculate_weather(wind, pressure, humidity)
    
    print(f"Generated Weather Data for Set {index + 1}:")
    for i in range(len(x_values)):
        print(f"x={x_values[i]}, y={y_values[i]}")

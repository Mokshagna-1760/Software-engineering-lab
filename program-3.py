import numpy as np
import pandas as pd

# Function to calculate weather data based on input parameters
def calculate_weather(wind, pressure, humidity):
    x = np.linspace(-10, 10, 100)
    y = wind * x**2 + pressure * x + humidity
    return x, y

# Read data from CSV file into a pandas DataFrame
data = pd.read_csv('program-3.csv')

# Iterate through each row in the DataFrame
for index, row in data.iterrows():
    # Extract values from the current row
    wind = row['a']
    pressure = row['b']
    humidity = row['c']
    
    # Call the calculate_weather function
    x_values, y_values = calculate_weather(wind, pressure, humidity)
    
    # Display generated weather data for the current set
    print(f"Generated Weather Data for Set {index + 1}:")
    for i in range(len(x_values)):
        print(f"  x={x_values[i]}, y={y_values[i]}") 

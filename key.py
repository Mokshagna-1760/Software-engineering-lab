import numpy as np

# Function to calculate weather data based on coefficients
def calculate_weather(a, b, c):
    # Generating 100 x values between -10 and 10
    x = np.linspace(-10, 10, 100)
    
    # Calculating y values using the coefficients for wind, pressure, and humidity
    y = a * x**2 + b * x + c  # Equation using coefficients for wind, pressure, and humidity
    return x, y

# Input coefficients from user
wind = float(input("Enter coefficient of wind: "))
pressure = float(input("Enter coefficient of pressure: "))
humidity = float(input("Enter coefficient of humidity: "))

# Calculate weather data
x_values, y_values = calculate_weather(wind, pressure, humidity)

# Display generated weather data for a single set of inputs
print("Generated Weather Data for a Single Set of Inputs:")
for i in range(len(x_values)):
    print(f"x={x_values[i]}, y={y_values[i]}")

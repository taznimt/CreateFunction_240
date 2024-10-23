#number1
def convert_temperature(value, unit):
    if unit.upper() == 'C':
        # Convert Celsius to Fahrenheit
        converted_value = (value * 9/5) + 32
        return converted_value, 'F'
    elif unit.upper() == 'F':
        # Convert Fahrenheit to Celsius
        converted_value = (value - 32) * 5/9
        return converted_value, 'C'
    else:
        raise ValueError("Invalid unit. Use 'C' for Celsius or 'F' for Fahrenheit.")

# User Input
try:
    temp_value = float(input("Enter the temperature value: "))
    temp_unit = input("Enter the temperature unit ('C' for Celsius, 'F' for Fahrenheit): ")

    converted_temp = convert_temperature(temp_value, temp_unit)
    print(f"{temp_value}°{temp_unit.upper()} is {converted_temp[0]:.2f}°{converted_temp[1]}")
except ValueError as e:
    print(e)
    
    #number2
import math

# Define the lambda function to calculate the area of a circle
circle_area = lambda r: math.pi * r**2

# Get user input for the radius
radius = float(input("Masukkan jari-jari lingkaran: "))

# Calculate the area using the lambda function
area = circle_area(radius)

# Print the result
print(f"Luas lingkaran dengan jari-jari {radius} adalah {area:.2f}")




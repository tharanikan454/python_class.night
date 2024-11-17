def convert_temperature(temperature, scale):
    if scale.upper() == 'C':
        # Convert Celsius to Fahrenheit
        return (temperature * 9/5) + 32
    elif scale.upper() == 'F':
        # Convert Fahrenheit to Celsius
        return (temperature - 32) * 5/9
    else:
        return "Invalid scale. Please use 'C' for Celsius or 'F' for Fahrenheit."

# Example usage
temp_in_celsius = 25
temp_in_fahrenheit = 77

converted_temp1 = convert_temperature(temp_in_celsius, 'C')
converted_temp2 = convert_temperature(temp_in_fahrenheit, 'F')

print(f"{temp_in_celsius}°C is {converted_temp1}°F")
print(f"{temp_in_fahrenheit}°F is {converted_temp2}°C")


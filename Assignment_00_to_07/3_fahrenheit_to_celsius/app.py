# Asking user for temperature in Fahrenheit
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Converting to Celsius
celsius = (fahrenheit - 32) * 5.0 / 9.0

# Printing the result
print(f"Temperature: {fahrenheit}F = {celsius}C")
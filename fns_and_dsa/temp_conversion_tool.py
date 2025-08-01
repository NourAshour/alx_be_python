FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (temp - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temp = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
if unit == "F":
    converted = convert_to_celsius(temp)
    print(f"{temp}°F is {converted}°C")
elif unit == "C":
    converted = convert_to_fahrenheit(temp)
    print(f"{temp}°C is {converted}°F")
else:
    print("Enter a valid unit.")
FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    x = fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"The temperature in celcius is {x}")
    return x

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    x = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR
    print(f"The temperature in fahrenheit is {x}")
    return x

temperature = input("Enter the temperature to convert: ")

temperature = float(temperature)

temperature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if temperature_type == 'F':
    convert_to_celsius(temperature)
elif temperature_type == 'C':
    convert_to_fahrenheit(temperature)
else:
    print("Please enter valid option")





# user_input = input("Enter the temperature to convert: ")

# convert_to_celsius(fahrenheit = "{fahrenheit_value}")
# temperaure = input("Is the entered temperature in Celsius or Fahrenheit? (C/F)")

# if temperaure == 'F':
#     convert_to_celsius(fahrenheit=user_input)
#     print(f"{user_input} f to celcius is: {}")
# elif temperaure == 'C':
#     convert_to_fahrenheit()


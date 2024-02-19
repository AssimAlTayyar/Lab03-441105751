def celsius_to_fahrenheit(celsius):
    return (9/5) * celsius + 32


while True:
    try:
        celsius_temp = float(input("Enter the temperature in Celsius: "))
        break
    except ValueError:
        print("Invalid input. Please enter a numerical value.")


fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)


print("\nThe temperature in Fahrenheit is:", fahrenheit_temp)

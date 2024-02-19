while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")


for i in range(1, 11):
    result = number * i
    print("{} x {} = {}".format(number, i, result))
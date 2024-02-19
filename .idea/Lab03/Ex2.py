def find_largest_number(lst):
    if not lst:
        return None  
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest


numbers = []


for i in range(10):
    while True:
        try:
            value = float(input("Enter value 12{}: ".format(i + 1)))
            break
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    numbers.append(value)


largest_number = find_largest_number(numbers)


if largest_number is not None:
    print("\nThe largest number is:", largest_number)
else:
    print("\nThe list is empty.")

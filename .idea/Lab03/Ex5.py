def repeat_decorator(num_repetitions):
    def decorator(func):
        def wrapper():
            for _ in range(num_repetitions):
                func()
        return wrapper
    return decorator


while True:
    try:
        x = int(input("Enter a number of repetitions: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")


@repeat_decorator(x)
def hello():
    print('Hello')

hello()

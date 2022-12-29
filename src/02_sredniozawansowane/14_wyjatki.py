def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("You cannot divide by zero!")
    else:
        print(f"{a} / {b} = {result}")
    finally:
        print("The divide function has finished executing.")


# This will execute successfully and print the result
divide(10, 2)

# This will raise a ZeroDivisionError exception
divide(10, 0)


class CustomException(Exception):
    def __init__(self, message):
        self.message = message


def validate_input(input_string):
    if len(input_string) < 5:
        raise CustomException("Input string must be at least 5 characters long.")


try:
    validate_input("abc")
except CustomException as e:
    print(e.message)


class NegativeNumberError(Exception):
    def __init__(self, number):
        self.number = number


def calculate_square(number):
    if number < 0:
        raise NegativeNumberError(number)
    return number ** 2


try:
    result = calculate_square(-10)
except NegativeNumberError as e:
    print(f"Cannot calculate square of negative number: {e.number}")

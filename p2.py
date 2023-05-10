import math


def divide_lbyl(num1: int | float, num2: int | float)-> float | str:
    """
    This function takes two numbers as input and returns the result of dividing
    the first number by the second number in the output, provided that there is no error.
    :param num1: first number
    :param num2: second number
    :return: num1/num2 or error text
    """

    if type(num1) !=(int or float) or type(num2) !=(int or float) :
        return "Value Error"

    if num2 == 0:  # Exceptional situation
        print("zero division detected")  # Error handling
        return math.inf
    return num1 / num2  # Most common situation


# Examples
print(divide_lbyl(8, 2))
print(divide_lbyl(8, 0))
print(divide_lbyl(8, "a"))


# -----------------------------------------------------------------------------------
print("-"*50)


def divide_eafp(num1: int | float, num2: int | float)-> float | str:
    """
    This function takes two numbers as input and returns the result of dividing
    the first number by the second number in the output, provided that there is no error.
    :param num1: first number
    :param num2: second number
    :return: num1/num2 or error text
    """
    try:
        return num1 / num2  # Most common situation
    except ZeroDivisionError:  # Exceptional situation
        print("zero division detected")  # Error handling
        return math.inf
    except ValueError:
        print("Value error")
    except TypeError:
        return "Type Error"


# Examples
print(divide_eafp(8, 2))
print(divide_eafp(8, 0))
print(divide_eafp(8, "0"))


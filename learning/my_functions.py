def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.

    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

def read_string_from_file(path) :
    file = open(path)
    return file.read()

def generic_procedure():
    print("This method returns nothing!")


def round_to_two_places(num):
    """Return the given number rounded to two decimal places.

    >>> round_to_two_places(3.14159)
    3.14
    """
    return round_to_n_places(num, 2)


def round_to_n_places(num, number_of_digits):
    """Return the given number rounded to number_of_digits decimal places.

    >>> round_to_two_places(3.14159, 4)
    3.1415
    """
    return round(num, number_of_digits)
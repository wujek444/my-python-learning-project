def sign(number):
    """
    Function takes a numerical argument and returns -1 if it's negative, 1 if it's positive, and 0 if it's 0.
    >>>sign(-2123.923)
    -1
    """
    if number == 0:
        return 0
    elif number > 0:
        return 1
    else:
        return -1

def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.

    >>> to_smash(91)
    1
    """
    print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")

    return total_candies % 3

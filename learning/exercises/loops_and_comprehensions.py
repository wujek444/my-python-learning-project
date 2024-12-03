def has_lucky_number(nums):
    return any([num % 7 == 0 for num in nums])

print("has_lucky_number([3, 5, 6, 7, 14]) =", has_lucky_number([3, 5, 6, 7, 14]))

#################

def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is
    True if L[i] is greater than thresh, and False otherwise.

    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    return [num > thresh for num in L]

print("elementwise_greater_than([1, 2, 3, 4] =", elementwise_greater_than([1, 2, 3, 4], 2))

#################

def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    previous_meal = None
    for meal in meals:
        if meal == previous_meal:
            return True
        previous_meal = meal
    return False

print("is menu boring?", menu_is_boring(["pizza", "calzone", "spaghetti", "pizza", "pizza", "calzone"]))
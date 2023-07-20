def reverse_str(initial_string):
    """_summary_
    returns the inverse of the initial string only if it consists of digits
    otherwise returns the initial string

    Args:
        initial_string (_type_): _description_

    Returns:
        _type_: _description_
    """
    if initial_string.isdigit():
        final_string = ''
        index = len(initial_string)
        while index > 0:
            final_string += initial_string[index - 1]
            index = index - 1
    else:
        final_string = initial_string
    return final_string


def is_prime(number):
    if number == 1:
        return False

    for x in range(2, number):
        if number % x == 0:
            return False
    return True

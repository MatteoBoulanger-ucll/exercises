import re
# Write your code here


def contains_three_digits(string):
    if re.fullmatch(".*[0-9]{3,}", string):
        return True
    else:
        return False

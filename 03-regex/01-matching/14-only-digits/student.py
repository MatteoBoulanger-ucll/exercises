# Write your code here
import re


def only_digits(string):
    if re.fullmatch("[1234567890]*", string):
        return True
    else:
        return False

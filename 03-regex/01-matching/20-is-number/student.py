# Write your code here
import re


def is_number(string):
    if re.fullmatch('[0-9]+(\.[0-9]+)?', string):
        return True
    else:
        return False

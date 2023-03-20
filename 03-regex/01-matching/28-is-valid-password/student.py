# Write your code here
import re


def is_valid_password(string):
    if re.fullmatch("([a-zA-Z0-9\+\-\*\/\.\@])+{12,}", string):
        return True
    else:
        return False

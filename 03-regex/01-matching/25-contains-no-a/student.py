# Write your code here
import re


def contains_no_a(string):
    if re.fullmatch('[^a]*', string):
        return True
    else:
        return False

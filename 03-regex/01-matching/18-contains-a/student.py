# Write your code here
import re


def contains_a(string):
    if re.search("a", string):
        return True
    else:
        return False

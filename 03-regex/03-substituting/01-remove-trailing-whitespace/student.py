# Write your code here
import re


def remove_trailing_whitespace(strings):
    return re.sub('\s+$', '', strings, flags=re.MULTILINE)

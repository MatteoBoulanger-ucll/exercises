import re
# Write your code here


def only_letters(string):
    if re.fullmatch("[a-zA-Z]*", string):
        return True
    else:
        return False

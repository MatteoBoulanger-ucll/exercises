# Write your code here
import re


def is_valid_email_address(string):
    if re.fullmatch("([a-z0-9]*\.*[a-z0-9]*)@(ucll.be|student.ucll.be)", string):
        return True
    else:
        return False

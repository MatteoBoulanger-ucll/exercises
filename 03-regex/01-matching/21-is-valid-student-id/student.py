# Write your code here
import re


def is_valid_student_id(string):
    if re.fullmatch("(s|r|S|R)[0-9]{7}", string):
        return True
    else:
        return False

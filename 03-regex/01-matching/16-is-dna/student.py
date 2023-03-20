# Write your code here
import re


def is_dna(string):
    if re.fullmatch("[G|A|T|C]*", string):
        return True
    else:
        return False

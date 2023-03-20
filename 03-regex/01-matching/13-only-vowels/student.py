# Write your code here
import re


def only_vowels(string):
    if re.fullmatch("[aeiou]*", string):
        return True
    else:
        return False


print(only_vowels("ae"))

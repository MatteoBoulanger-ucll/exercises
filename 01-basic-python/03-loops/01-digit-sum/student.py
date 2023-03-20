# Write your code here
def last_digit(number):
    return number % 10


def remove_last_digit(number):
    return number // 10


def digit_sum(number):
    result = 0
    while number > 0:
        result += last_digit(number)
        number = remove_last_digit(number)
    return result

# Write your code here
def is_prime(number):
    for getal in range(2, number):
        if number % getal == 0:
            return False

    return number > 1

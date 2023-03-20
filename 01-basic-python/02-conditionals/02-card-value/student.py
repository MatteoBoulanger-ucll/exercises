# Write your code here
def card_value(string):
    number = 0
    if string == 'Jack':
        number = 11
    elif string == "Queen":
        number = 12
    elif string == "King":
        number = 13
    elif string == "Ace":
        number = 1
    else:
        number = int(string)

    return number

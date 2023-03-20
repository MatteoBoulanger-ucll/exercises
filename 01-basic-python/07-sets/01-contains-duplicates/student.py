# Write your code here
def contains_duplicates(lst):
    if len(lst) > len(set(lst)):
        return True
    else:
        return False

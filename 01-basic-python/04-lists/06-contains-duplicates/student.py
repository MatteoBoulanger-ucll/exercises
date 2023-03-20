# Write your code here
def contains_duplicates(lijst):
    dubbel = False
    for element in lijst:
        if lijst.count(element) > 1:
            dubbel = True

    return dubbel
